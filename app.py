import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #8E2DE2, #FF6FD8);
    color: white;
    font-family: 'Poppins', sans-serif;
}

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #f1f1f1;
    margin-bottom: 35px;
}

.glass {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 25px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

.stTextArea textarea {
    border-radius: 15px;
    background: rgba(255,255,255,0.12);
    color: white;
}

.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.12);
    border-radius: 12px;
}

.stButton>button {
    width: 100%;
    height: 52px;
    border-radius: 15px;
    border: none;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(to right, #00F5A0, #00D9F5);
    color: black;
}

.stButton>button:hover {
    transform: scale(1.02);
}

.output-box {
    background: rgba(255,255,255,0.18);
    padding: 22px;
    border-radius: 18px;
    margin-top: 25px;
    font-size: 22px;
}

.detect-box {
    background: rgba(0,0,0,0.2);
    padding: 12px;
    border-radius: 12px;
    margin-top: 15px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>🌍 AI Language Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Translate any language instantly using AI 🚀</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("✨ Features")

st.sidebar.info("""
✅ Auto Language Detection  
✅ AI Translation  
✅ Text to Speech  
✅ Download Translation  
✅ Translation History  
""")

st.sidebar.markdown("---")
st.sidebar.write("👩‍💻 Developed by Aliya Afzal")

# ---------------- LANGUAGES ----------------
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru"
}

# ---------------- MAIN UI ----------------
with st.container():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    text = st.text_area(
        "✍ Enter Text",
        height=200,
        placeholder="Type any language here..."
    )

    target_lang = st.selectbox(
        "🌍 Translate To",
        list(languages.keys())
    )

    if st.button("🚀 Translate Now"):

        if text.strip() == "":
            st.warning("⚠ Please enter text")

        else:
            try:

                # -------- AUTO DETECT --------
                detected_lang = detect(text)

                detected_name = "Unknown"

                for lang_name, lang_code in languages.items():
                    if lang_code.startswith(detected_lang):
                        detected_name = lang_name

                st.markdown(
                    f"""
                    <div class='detect-box'>
                    🔍 Detected Language: <b>{detected_name}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # -------- TRANSLATION --------
                translated = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text)

                st.markdown(
                    f"""
                    <div class='output-box'>
                    <b>✨ Translated Text:</b><br><br>
                    {translated}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # -------- AUDIO --------
                tts = gTTS(translated)
                tts.save("translation.mp3")

                audio_file = open("translation.mp3", "rb")
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format="audio/mp3")

                # -------- DOWNLOAD --------
                st.download_button(
                    label="⬇ Download Translation",
                    data=translated,
                    file_name="translated_text.txt",
                    mime="text/plain"
                )

                # -------- HISTORY --------
                current_time = datetime.now().strftime("%H:%M:%S")

                if "history" not in st.session_state:
                    st.session_state.history = []

                st.session_state.history.append(
                    {
                        "time": current_time,
                        "input": text,
                        "output": translated
                    }
                )

            except:
                st.error("❌ Translation Failed")

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------- FOOTER ----------------
st.markdown("""
<br><br>
<center>
✨ Built with Streamlit & AI
</center>
""", unsafe_allow_html=True)
