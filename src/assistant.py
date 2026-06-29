import random
import webbrowser
from datetime import datetime

from services import WEB_SERVICES


class Assistant:
    def __init__(self, name: str = "Alice") -> None:
        self.name = name
        self._jokes: list[str] = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
        ]

    def handle(self, user_input: str) -> str:
        text = user_input.lower()

        if "what is your name" in text:
            return f"My name is {self.name}."
        if "who are you" in text:
            return "I am your cheerful virtual assistant!"
        if "hello" in text or "hi" in text:
            return "Hello there! 😊 How can I assist you today?"
        if "good morning" in text:
            return "Good morning! Wishing you a productive day ahead!"
        if "good afternoon" in text:
            return "Good afternoon! What can I help you with?"
        if "shutdown" in text:
            return "Alright, shutting down. See you soon!"

        for service in WEB_SERVICES:
            if any(kw in text for kw in service.keywords):
                webbrowser.open(service.url)
                return service.response

        if "time now" in text:
            now = datetime.now()
            return f"The current time is {now.strftime('%H:%M:%S')}"
        if "joke" in text:
            return random.choice(self._jokes)

        return "Hmm, I didn't catch that. Can you please repeat?"
