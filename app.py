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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #ff758c 100%);
    background-attachment: fixed;
    color: white;
}

/* Hide Streamlit menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 700;
    color: white;
    margin-top: 15px;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: rgba(255,255,255,0.85);
    margin-bottom: 40px;
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.12);
    padding: 35px;
    border-radius: 28px;
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 8px 32px rgba(0,0,0,0.18);
}

/* Text Area */
.stTextArea textarea {
    border-radius: 18px !important;
    background: rgba(255,255,255,0.10) !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    font-size: 18px !important;
    padding: 15px !important;
}

.stTextArea textarea::placeholder {
    color: rgba(255,255,255,0.6) !important;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.10) !important;
    border-radius: 14px !important;
    color: white !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 16px;
    border: none;
    font-size: 19px;
    font-weight: 600;
    background: linear-gradient(to right, #00F5A0, #00D9F5);
    color: #111;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.15);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}

/* Detection Box */
.detect-box {
    background: rgba(255,255,255,0.12);
    padding: 14px;
    border-radius: 14px;
    margin-top: 18px;
    font-size: 17px;
    border-left: 4px solid #00F5A0;
}

/* Output Box */
.output-box {
    background: rgba(255,255,255,0.15);
    padding: 24px;
    border-radius: 18px;
    margin-top: 25px;
    font-size: 22px;
    line-height: 1.7;
    border: 1px solid rgba(255,255,255,0.18);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(15,15,25,0.65);
    backdrop-filter: blur(16px);
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 45px;
    color: rgba(255,255,255,0.85);
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class='main-title'>🌍 AI Language Translator</div>
    <div class='subtitle'>
    Translate any language instantly using AI and connect beyond language barriers ✨
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("✨ App Features")

st.sidebar.markdown("""
### 🌟 Features
✅ Auto Language Detection  
✅ AI Translation  
✅ Text to Speech  
✅ Download Translation  
✅ Premium Glassmorphism UI  

---
### 👩‍💻 Developer
Aliya Afzal
""")

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
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

text = st.text_area(
    "✍ Enter Text",
    height=220,
    placeholder="Type or paste text in any language..."
)

target_lang = st.selectbox(
    "🌍 Translate To",
    list(languages.keys())
)

# ---------------- TRANSLATE BUTTON ----------------
if st.button("🚀 Translate Now"):

    if text.strip() == "":
        st.warning("⚠ Please enter some text")

    elif len(text.strip()) < 2:
        st.warning("⚠ Please enter more text for accurate detection")

    else:
        try:

            # -------- DETECT LANGUAGE --------
            detected_lang = detect(text)

            language_names = {
                "en": "English",
                "hi": "Hindi",
                "fr": "French",
                "de": "German",
                "es": "Spanish",
                "ar": "Arabic",
                "zh-cn": "Chinese",
                "ja": "Japanese",
                "ko": "Korean",
                "ru": "Russian"
            }

            detected_name = language_names.get(
                detected_lang.lower(),
                detected_lang.upper()
            )

            st.markdown(
                f"""
                <div class='detect-box'>
                🔍 Detected Language: <b>{detected_name}</b>
                </div>
                """,
                unsafe_allow_html=True
            )

            # -------- LOADING --------
            with st.spinner("✨ Translating your text..."):

                translated = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text)

            # -------- OUTPUT --------
            st.markdown(
                f"""
                <div class='output-box'>
                <b>✨ Translated Text</b><br><br>
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

        except Exception as e:
            st.error("❌ Translation failed. Please try again.")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class='footer'>
    ✨ Built with Streamlit & AI
    </div>
    """,
    unsafe_allow_html=True
)
