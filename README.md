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

## Usage

### Basic Usage:
Here's a simple example to get you started with SpeechToTextNow:
```python
stt_now = SpeechToTextNow()
stt_now.listen()
```
### Callback
SpeechToTextNow supports a callback function for custom handling of the transcription results. This can be useful for integrating with other applications or processing the text further.

Here's how to use the callback feature:
```python
def my_custom_callback(transcribed_text):
    print("Received transcription:", transcribed_text)

stt_now = SpeechToTextNow(callback=my_custom_callback)
stt_now.listen()
```
## Configuration

You can customize SpeechToTextNow's behavior by modifying the following parameters:

- **vad_mode**: (int, default=1) Adjust the aggressiveness of voice activity detection. Range: 0 (least aggressive) to 3 (most aggressive).
- **channels**: (int, default=1) Number of audio channels (1 for mono, 2 for stereo).
- **rate**: (int, default=16000) Sampling rate in Hz.
- **chunk_duration_ms**: (int, default=30) Duration of audio chunks to process, in milliseconds.
- **padding_duration_ms**: (int, default=300) Duration of padding (silence) used for VAD triggering, in milliseconds.
- **stt_engine**: (str, default="google_stt") Choose between "google_stt" and "openai_stt" for the speech recognition engine.
- **callback**: (function, default=None) A function that will be called with the transcribed text as its argument.

## Contributing

Contributions to SpeechToTextNow are welcome! Feel free to fork the project, make improvements, and submit a pull request with your changes.

## Acknowledgments
- WebRTC for voice activity detection capabilities.
- PyAudio for handling audio streams.
- The Google Speech Recognition API for transcription services.
