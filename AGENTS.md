# Agents

## Run

```bash
streamlit run src/main.py
```

Install deps: `pip install -r requirements.txt`

## Structure

```
src/
  __init__.py
  main.py       Streamlit UI entrypoint
  assistant.py  Assistant class with intent dispatch
  speech.py     speech_to_text / text_to_speech (singleton engine)
```

No tests, no lint/typecheck config, no CI.

## Key facts

- Assistant name is **Alice**, hardcoded in `assistant.py:8` (`Assistant.__init__` default).
- Speech-to-text via `speech_recognition` (Google API, requires microphone); TTS via `pyttsx3` (offline, singleton engine).
- Web commands open URLs via `webbrowser.open` — no browser automation.
- All deps are listed in `requirements.txt` and must be installed manually.
