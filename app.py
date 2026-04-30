import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Translator",
    page_icon="🌍",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #fc5c7d, #6a82fb);
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
    padding: 35px;
    border-radius: 25px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

.stTextArea textarea {
    border-radius: 18px;
    background: rgba(255,255,255,0.12);
    color: white;
    font-size: 18px;
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
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
}

.output-box {
    background: rgba(255,255,255,0.18);
    padding: 25px;
    border-radius: 18px;
    margin-top: 25px;
    font-size: 22px;
    color: white;
}

.detect-box {
    background: rgba(0,0,0,0.2);
    padding: 12px;
    border-radius: 12px;
    margin-top: 15px;
    font-size: 18px;
}

.footer {
    text-align:center;
    margin-top:40px;
    color:white;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>🌍 AI Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Translate any language instantly with AI 🚀</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("✨ Features")

st.sidebar.info("""
✅ Auto Language Detection  
✅ AI Translation  
✅ Text to Speech  
✅ Download Translation  
✅ Modern Glassmorphism UI  
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

# ---------------- MAIN CARD ----------------
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

# ---------------- TRANSLATE ----------------
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("⚠ Please enter text")

    else:
        try:

            # -------- DETECT LANGUAGE --------
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

            # -------- LOADING --------
            with st.spinner("Translating..."):

                translated = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text)

            # -------- OUTPUT --------
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

        except:
            st.error("❌ Translation Failed")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>✨ Built with Streamlit & AI</div>",
    unsafe_allow_html=True
)
