import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Language Translator",
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

/* Background */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 45%, #ff758c 100%);
    color: white;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 700;
    color: white;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: rgba(255,255,255,0.88);
    margin-bottom: 35px;
}

/* Input Box */
.stTextArea textarea {
    background: rgba(255,255,255,0.18) !important;
    color: white !important;
    border-radius: 22px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    padding: 18px !important;
    font-size: 18px !important;
    backdrop-filter: blur(8px);
}

.stTextArea textarea::placeholder {
    color: rgba(255,255,255,0.65);
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.18) !important;
    border-radius: 16px !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Translate Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 16px;
    font-size: 19px;
    font-weight: 600;
    color: black;
    background: linear-gradient(to right, #00F5A0, #00D9F5);
    transition: 0.3s ease;
    box-shadow: 0 4px 18px rgba(0,0,0,0.18);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* Detection Card */
.detect-card {
    background: rgba(255,255,255,0.18);
    padding: 15px;
    border-radius: 18px;
    margin-top: 25px;
    border-left: 5px solid #00F5A0;
    font-size: 18px;
}

/* Output Card */
.output-card {
    background: rgba(255,255,255,0.20);
    padding: 28px;
    border-radius: 24px;
    margin-top: 25px;
    border: 1px solid rgba(255,255,255,0.22);
    font-size: 22px;
    line-height: 1.8;
    color: white;
    backdrop-filter: blur(10px);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(18,18,30,0.65);
    backdrop-filter: blur(18px);
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
st.markdown("""
<div class='main-title'>🌍 AI Language Translator</div>
<div class='subtitle'>
Translate any language instantly using AI and connect beyond language barriers ✨
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("✨ Features")

st.sidebar.markdown("""
### 🌟 App Features

✅ Auto Language Detection  
✅ Real-Time AI Translation  
✅ Text-to-Speech  
✅ Download Translation  
✅ Modern Glassmorphism UI  

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

# ---------------- INPUT ----------------
text = st.text_area(
    "✍ Enter Text",
    height=220,
    placeholder="Type or paste text in any language..."
)

target_lang = st.selectbox(
    "🌐 Translate To",
    list(languages.keys())
)

# ---------------- CENTER BUTTON ----------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    translate = st.button("🚀 Translate Now")

# ---------------- TRANSLATION ----------------
if translate:

    if text.strip() == "":
        st.warning("⚠ Please enter some text")

    else:

        try:

            # -------- SMART DETECTION --------
            if len(text.split()) < 3:
                detected_lang = "en"
            else:
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

            # -------- DETECTED LANGUAGE --------
            st.markdown(
                f"""
                <div class='detect-card'>
                🔍 <b>Detected Language:</b> {detected_name}
                </div>
                """,
                unsafe_allow_html=True
            )

            # -------- LOADING --------
            with st.spinner("✨ Translating..."):

                translated = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text)

            st.toast("Translation completed ✨")

            # -------- OUTPUT --------
            st.markdown(
                f"""
                <div class='output-card'>
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

        except:
            st.error("❌ Translation failed. Please try again.")

# ---------------- FOOTER ----------------
st.markdown("""
<div class='footer'>
✨ Built with Streamlit & AI
</div>
""", unsafe_allow_html=True)
