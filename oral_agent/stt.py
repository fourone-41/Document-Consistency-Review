import numpy as np
import speech_recognition as sr


def transcribe(audio_tuple: tuple) -> str:
    """
    Convert Gradio microphone audio (numpy format) to English text.
    audio_tuple: (sample_rate: int, data: np.ndarray) from gr.Audio(type="numpy")
    Raises sr.UnknownValueError if speech is not understood.
    Raises sr.RequestError if Google STT is unreachable.
    """
    sample_rate, audio_data = audio_tuple

    if audio_data.dtype in (np.float32, np.float64):
        audio_data = (audio_data * 32767).clip(-32768, 32767).astype(np.int16)
    elif audio_data.dtype != np.int16:
        audio_data = audio_data.astype(np.int16)

    if audio_data.ndim == 2:
        audio_data = audio_data[:, 0]

    recognizer = sr.Recognizer()
    audio = sr.AudioData(
        audio_data.tobytes(),
        sample_rate=sample_rate,
        sample_width=2,
    )
    return recognizer.recognize_google(audio, language="en-US")
