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
    background: linear-gradient(135deg, #e0c3fc 0%, #8ec5fc 100%);
    color: #2d2d2d;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 58px;
    font-weight: 700;
    color: #222;
    margin-top: 20px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #444;
    margin-bottom: 40px;
}

/* Labels */
label {
    color: #2d2d2d !important;
    font-weight: 600 !important;
    font-size: 18px !important;
}

/* Text Area */
.stTextArea textarea {
    background: rgba(255,255,255,0.75) !important;
    color: #222 !important;
    border-radius: 20px !important;
    border: 1px solid rgba(255,255,255,0.4) !important;
    padding: 18px !important;
    font-size: 18px !important;
    backdrop-filter: blur(8px);
}

.stTextArea textarea::placeholder {
    color: #666 !important;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"] {
    background: rgba(255,255,255,0.75) !important;
    border-radius: 16px !important;
    border: 1px solid rgba(255,255,255,0.4);
}

.stSelectbox * {
    color: #222 !important;
    font-weight: 500;
}

/* Translate Button */
.stButton > button {
    width: 100%;
    height: 55px;
    border: none;
    border-radius: 16px;
    font-size: 18px;
    font-weight: 600;
    color: white;
    background: linear-gradient(to right, #6a5acd, #7b68ee);
    transition: 0.3s ease;
    box-shadow: 0 4px 18px rgba(0,0,0,0.12);
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* Download Button */
.stDownloadButton > button {
    width: 100%;
    height: 52px;
    border-radius: 16px;
    border: none;
    font-size: 17px;
    font-weight: 600;
    background: linear-gradient(to right, #6a5acd, #7b68ee);
    color: white !important;
    margin-top: 15px;
}

/* Detection Card */
.detect-card {
    background: rgba(255,255,255,0.45);
    padding: 15px;
    border-radius: 18px;
    margin-top: 25px;
    border-left: 5px solid #6a5acd;
    font-size: 18px;
    color: #222;
}

/* Output Card */
.output-card {
    background: rgba(255,255,255,0.45);
    padding: 28px;
    border-radius: 24px;
    margin-top: 25px;
    border: 1px solid rgba(255,255,255,0.4);
    font-size: 20px;
    line-height: 1.8;
    color: #222;
    backdrop-filter: blur(10px);
    min-height: 120px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(14px);
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 45px;
    color: #444;
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
✅ Modern Professional UI  

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

# ---------------- BUTTON ----------------
col1, col2, col3 = st.columns([1,2,1])

with col2:
    translate = st.button("🚀 Translate Now")

# ---------------- TRANSLATION ----------------
if translate:

    if text.strip() == "":
        st.warning("⚠ Please enter some text")

    else:

        try:

            # Smart English Detection
            common_english_words = [
                "hello", "hi", "i", "am", "my",
                "name", "how", "are", "you",
                "what", "is"
            ]

            text_lower = text.lower()

            if any(word in text_lower for word in common_english_words):
                detected_lang = "en"
            else:
                detected_lang = detect(text)

            # Language Names
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

            # Detection Card
            st.markdown(
                f"""
                <div class='detect-card'>
                🔍 <b>Detected Language:</b> {detected_name}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Translation
            with st.spinner("✨ Translating..."):

                translated = GoogleTranslator(
                    source='auto',
                    target=languages[target_lang]
                ).translate(text)

            st.toast("Translation completed ✨")

            # Output Card
            st.markdown(
                f"""
                <div class='output-card'>
                <b>✨ Translated Text</b><br><br>
                {translated}
                </div>
                """,
                unsafe_allow_html=True
            )

            # Audio
            tts = gTTS(translated)
            tts.save("translation.mp3")

            audio_file = open("translation.mp3", "rb")
            audio_bytes = audio_file.read()

            st.audio(audio_bytes, format="audio/mp3")

            # Download Button
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
