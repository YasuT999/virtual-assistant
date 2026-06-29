import speech_recognition as sr
import pyttsx3
from typing import Optional

_engine: Optional[pyttsx3.Engine] = None


def _get_tts_engine() -> pyttsx3.Engine:
    global _engine
    if _engine is None:
        _engine = pyttsx3.init()
        _engine.setProperty("rate", 150)
    return _engine


def speech_to_text() -> Optional[str]:
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
        return recognizer.recognize_google(audio)
    except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError):
        return None


def text_to_speech(text: str) -> None:
    engine = _get_tts_engine()
    engine.say(text)
    engine.runAndWait()
