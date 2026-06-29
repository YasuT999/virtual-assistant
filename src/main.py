import streamlit as st
from datetime import datetime
from streamlit_option_menu import option_menu

from assistant import Assistant
from services import WEB_SERVICES
from speech import speech_to_text, text_to_speech


st.set_page_config(page_title="✨ Virtual Assistant ✨", layout="wide")

if "assistant" not in st.session_state:
    st.session_state.assistant = Assistant()

if "history" not in st.session_state:
    st.session_state.history = []

now = datetime.now()
st.sidebar.image(
    "https://media.giphy.com/media/3o7TKxohkk8v3dPsAw/giphy.gif", width=150
)
st.sidebar.markdown(
    f"🕒 **{now.strftime('%A, %d %B %Y %H:%M:%S')}**"
)

menu = ["Home", "Assistance", "About"]
with st.sidebar:
    choice = option_menu(
        "Categories", menu,
        icons=["house", "mic", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if choice == "Home":
    st.title("🤖 Welcome to Alice - Your Virtual Assistant")
    st.markdown("""
        ## 👋 Hello There!
        Meet **Alice**, your always-ready AI assistant. Ask her anything!

        ### 🧠 Features:
        - Speech & Text commands
        - Weather forecast with icons
        - Web browsing assistant
        - Jokes & fun responses

        👉 Head to the **Assistance** tab to start talking with Alice!
    """)

elif choice == "Assistance":
    st.title("🧠 Talk to Alice")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✍️ Type a message")
        user_input = st.text_input(
            "You:", placeholder="Type here and press enter..."
        )
        if st.button("Send") and user_input:
            assistant: Assistant = st.session_state.assistant
            response = assistant.handle(user_input)
            text_to_speech(response)
            st.session_state.history.append((user_input, response))

    with col2:
        st.subheader("🎤 Speak to Alice")
        if st.button("Speak Now"):
            st.info("🎙️ Listening...")
            spoken_text = speech_to_text()
            if spoken_text:
                st.success(f"✅ You said: {spoken_text}")
                assistant: Assistant = st.session_state.assistant
                response = assistant.handle(spoken_text)
                text_to_speech(response)
                st.session_state.history.append((spoken_text, response))
            else:
                st.warning("Could not understand your speech. Try again!")

    st.divider()
    st.subheader("📝 Conversation History")
    for user, bot in st.session_state.history:
        st.markdown(f"**You:** {user}")
        st.markdown(f"**Alice:** {bot}")

elif choice == "About":
    st.title("📘 About This App")
    st.markdown("""
        **Virtual Assistant Alice** is a fun, interactive AI helper built using:
        - 🐍 Python
        - 🎙 Speech Recognition
        - 🔊 Text-to-Speech
        - 🌐 Streamlit for Web UI

        Created with ❤️ by pepakayala. Alice is designed to make your digital tasks
        easier & more enjoyable!
    """)

    st.subheader("🔗 Useful Links")
    for service in WEB_SERVICES:
        st.markdown(f"[🌍 {service.name}]({service.url})")
