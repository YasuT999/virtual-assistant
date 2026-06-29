from dataclasses import dataclass


@dataclass
class WebService:
    name: str
    url: str
    keywords: list[str]
    response: str


WEB_SERVICES: list[WebService] = [
    WebService("Google", "https://google.com", ["google"], "Google is at your service!"),
    WebService("Spotify", "https://open.spotify.com", ["play music"], "Spotify is all set! Enjoy your tunes 🎶"),
    WebService("YouTube", "https://youtube.com", ["youtube"], "YouTube is ready for you!"),
    WebService("ChatGPT", "https://chatgpt.com", ["chatgpt"], "Opening ChatGPT for you!"),
]
