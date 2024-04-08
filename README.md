# SpeechToTextNow

SpeechToTextNow is a realtime speech-to-text tool designed to transcribe voice into text.

## Features

- **Real-time Voice Activity Detection**: Quickly identifies speech in live audio streams, allowing for accurate start and stop recognition.
- **Continuous Listening**: Seamlessly listens and transcribes speech without interrupting the audio stream.
- **Parallel Processing**: Utilizes threading to handle transcription in parallel with audio capture.
- **Speech Segmentation and Queuing**: Manages speech segments in a queue for orderly processing.
- **Google Speech Recognition**: Leverages Google's powerful speech recognition API

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

## Using the SpeechToTextNow Class

You can integrate SpeechToTextNow into your own Python projects by creating an instance of the SpeechToTextNow class and calling the listen method. Here's a simple example:

```python
# Initialize SpeechToTextNow
sttn = SpeechToTextNow(
    channels=1, 
    rate=16000, 
    chunk_duration_ms=30,
    padding_duration_ms=300
)

# Start listening and transcribing in real-time
sttn.listen()
```

## Configuration

You can customize SpeechToTextNow's behavior by modifying the following parameters:

- **vad_mode**: Adjust the aggressiveness of voice activity detection. Range: 0 (least aggressive) to 3 (most aggressive).
- **channels**: Number of audio channels (1 for mono, 2 for stereo).
- **rate**: Sampling rate in Hz.
- **chunk_duration_ms**: Duration of audio chunks to process, in milliseconds.
- **padding_duration_ms**: Duration of padding (silence) used for VAD triggering, in milliseconds.

## Contributing

Contributions to SpeechToTextNow are welcome! Feel free to fork the project, make improvements, and submit a pull request with your changes.

## Acknowledgments
- WebRTC for voice activity detection capabilities.
- PyAudio for handling audio streams.
- The Google Speech Recognition API for transcription services.
