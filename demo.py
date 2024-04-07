import pyaudio
import wave
import webrtcvad
import collections
import speech_recognition as sr
import io
import queue
import threading

class SpeechToTextNow:
    def __init__(
            self, 
            vad_mode=1, 
            channels=1, 
            rate=16000, 
            chunk_duration_ms=30, 
            padding_duration_ms=300
            ):
        self.vad = webrtcvad.Vad(vad_mode)
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = channels
        self.RATE = rate
        self.CHUNK_DURATION_MS = chunk_duration_ms
        self.PADDING_DURATION_MS = padding_duration_ms
        self.CHUNK_SIZE = int(self.RATE * self.CHUNK_DURATION_MS / 1000)
        self.CHUNK_BYTES = self.CHUNK_SIZE * 2
        self.NUM_PADDING_CHUNKS = int(self.PADDING_DURATION_MS / self.CHUNK_DURATION_MS)
        self.audio = pyaudio.PyAudio()  
        self.device_index, self.device_name = self.find_microphone()
        print(self.device_index, self.device_name)
        self.stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                      rate=self.RATE, input=True, input_device_index=self.device_index,
                                      frames_per_buffer=self.CHUNK_SIZE)
    
        self.speech_segments_queue = queue.Queue()

    def find_microphone(self):
        keywords = ["Microphone", "Mic", "Input", "Line In"]
        p = pyaudio.PyAudio()

        for keyword in keywords:
            for i in range(p.get_device_count()):
                dev = p.get_device_info_by_index(i)
                if keyword.lower() in dev['name'].lower():
                    return i, dev['name']
                
        return None, "No matching device found."

    def save_speech(self, voiced_frames, sample_rate):
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(sample_rate)
            wf.writeframes(b''.join(voiced_frames))
        buffer.seek(0)
        return buffer
    
    def transcribe_audio(self, audio_buffer):
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_buffer) as source:
            audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data)
                print(f"{text}")
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Could not transcribe audio; {e}")

    def listen(self):
        ring_buffer = collections.deque(maxlen=self.NUM_PADDING_CHUNKS)
        voiced_frames = []
        triggered = False
        print("Listening...")
        try:
            while True:
                chunk = self.stream.read(self.CHUNK_SIZE)
                is_speech = self.vad.is_speech(chunk, self.RATE)
                
                if not triggered:
                    ring_buffer.append(chunk)
                    num_voiced = len([frame for frame in ring_buffer if self.vad.is_speech(frame, self.RATE)])
                    if num_voiced > 0.9 * ring_buffer.maxlen:
                        #print("Start Recording")
                        triggered = True
                        voiced_frames = list(ring_buffer)
                        ring_buffer.clear()
                else:
                    voiced_frames.append(chunk)
                    ring_buffer.append(chunk)
                    num_unvoiced = len([frame for frame in ring_buffer if not self.vad.is_speech(frame, self.RATE)])
                    if num_unvoiced > 0.9 * ring_buffer.maxlen:
                        #print("End Recording")
                        triggered = False
                        self.speech_segments_queue.put(voiced_frames)
                        threading.Thread(target=self.start_queue).start()
                        voiced_frames = []
        finally:
            self.stream.stop_stream()
            self.stream.close()
            self.audio.terminate()
    
    def start_queue(self):
        while not self.speech_segments_queue.empty():
            voiced_frames = self.speech_segments_queue.get()
            audio_buffer = self.save_speech(voiced_frames, self.RATE)
            self.transcribe_audio(audio_buffer)
            self.speech_segments_queue.task_done()

if __name__ == "__main__":
        
    sttn=SpeechToTextNow(
        channels=1, rate=16000, 
        chunk_duration_ms=30,
        padding_duration_ms=300
    )

    sttn.listen()