"""
Ears + Mouth, wrapped as reusable functions. Same mechanism as your
Combined.py - record with sounddevice, transcribe with Whisper,
speak with Orpheus + pyaudio.
"""
import os
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
from config import client, STT_MODEL, TTS_MODEL, TTS_VOICE
from utils import call_with_retry

def transcribe_audio():
    with open(RECORDING_PATH, "rb") as audio_file:
        transcription = call_with_retry(
            client.audio.transcriptions.create,
            file=audio_file,
            model=STT_MODEL
        )
    return transcription.text


def speak(text: str):
    response = call_with_retry(
        client.audio.speech.create,
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text,
        response_format="wav"
    )
    audio_data = response.read()


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORDING_PATH = os.path.join(BASE_DIR, "live_input.wav")


def record_audio(duration=5, sample_rate=44100):
    print("Listening...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    write(RECORDING_PATH, sample_rate, recording)


def transcribe_audio():
    with open(RECORDING_PATH, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=STT_MODEL
        )
    return transcription.text


def speak(text: str):
    response = client.audio.speech.create(
        model=TTS_MODEL,
        voice=TTS_VOICE,
        input=text,
        response_format="wav"
    )
    audio_data = response.read()

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(2), channels=1, rate=24000, output=True)
    stream.write(audio_data[44:])
    stream.stop_stream()
    stream.close()
    p.terminate()
