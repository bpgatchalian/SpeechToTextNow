# SpeechToTextNow

SpeechToTextNow is a realtime speech-to-text tool designed to transcribe voice into text.

## Features

- **Real-time Voice Activity Detection**: Quickly identifies speech in live audio streams, allowing for accurate start and stop recognition.
- **Continuous Listening**: Seamlessly listens and transcribes speech without interrupting the audio stream.
- **Parallel Processing**: Utilizes threading to handle transcription in parallel with audio capture.
- **Speech Segmentation and Queuing**: Manages speech segments in a queue for orderly processing.
- **Google Speech Recognition**: Leverages Google's powerful speech recognition API
- **OpenAI API Speech to Text (Whisper)**: Leverages OpenAI's state-of-the-art Whisper model for highly accurate speech-to-text transcription.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9 or higher

Additionally, you will need:

- An API key from OpenAI if you intend to use OpenAI's speech-to-text API.

## Installation

To use SpeechToTextNow, you'll need Python 3.6 or later. 

1. Begin by cloning the repository.
```sh
https://github.com/bpgatchalian/SpeechToTextNow.git
```
2. Navigate to the project directory.
```sh
cd SpeechToTextNow
```
3. Install the required dependencies.
```sh
pip install - requirements.txt
```
4. Run demo.py
```sh
"python demo.py"
```
Make sure your microphone is connected and configured as the default recording device. SpeechToTextNow will automatically start listening and transcribing in real-time.

## Usage

### Quick Start with listen()
For a quick start, simply create an instance of SpeechToTextNow and call the listen() method. This will block the execution and continuously transcribe speech until manually stopped or interrupted:
```python
stt_now = SpeechToTextNow()
stt_now.listen()
```
This approach is straightforward and ideal for testing or simple scripts where concurrent tasks are not needed while listening.

### Using start_listening() and stop_listening()
For more control and to enable concurrent execution in your application, use the **start_listening()** and **stop_listening()** methods. This allows SpeechToTextNow to run in the background:
```python
stt_now = SpeechToTextNow()

stt_now.start_listening() # start listening

stt_now.stop_listening() # call when ready to stop listening
```
### Handling Transcriptions with Callbacks
SpeechToTextNow supports the use of a callback function to process the transcription results in real-time. This is particularly useful for applications requiring immediate action upon transcription:
```python
def my_custom_callback(transcribed_text):
    print("Received transcription:", transcribed_text)

stt_now = SpeechToTextNow(transcription_callback=my_custom_callback)

stt_now.start_listening() # start listening

stt_now.stop_listening() # call when ready to stop listening
```
## Configuration

You can customize SpeechToTextNow's behavior by modifying the following parameters:

- **vad_mode**: (int, default=1) Adjust the aggressiveness of voice activity detection. Range: 0 (least aggressive) to 3 (most aggressive).
- **channels**: (int, default=1) Number of audio channels (1 for mono, 2 for stereo).
- **rate**: (int, default=16000) Sampling rate in Hz.
- **chunk_duration_ms**: (int, default=30) Duration of audio chunks to process, in milliseconds.
- **padding_duration_ms**: (int, default=300) Duration of padding (silence) used for VAD triggering, in milliseconds.
- **stt_engine**: (str, default="google_stt") Choose between "google_stt" and "openai_stt" for the speech recognition engine.
- **transcription_callback**: (function, default=None) A function that will be called with the transcribed text as its argument.

## Contributing

Contributions to SpeechToTextNow are welcome! Feel free to fork the project, make improvements, and submit a pull request with your changes.

## Acknowledgments
- WebRTC for voice activity detection capabilities.
- PyAudio for handling audio streams.
- The Google Speech Recognition API for transcription services.
