import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import base64
import os
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
    font-family: 'Poppins', sans-serif;
}

.main-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #dcdcdc;
    margin-bottom: 30px;
}

.glass {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #0072ff, #00c6ff);
    color: white;
}

.output-box {
    background: rgba(255,255,255,0.15);
    padding: 20px;
    border-radius: 15px;
    font-size: 20px;
    margin-top: 20px;
}

.sidebar .sidebar-content {
    background: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<div class='main-title'>🌍 AI Language Translator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Translate text instantly with AI-powered NLP technology 🚀</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 About App")

st.sidebar.info("""
### 🌟 Features
✅ Real-time Translation  
✅ Multiple Languages  
✅ AI-powered NLP  
✅ Text-to-Speech  
✅ Beautiful UI  

### 👩‍💻 Developer
Aliya Afzal
""")

st.sidebar.markdown("---")

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

# ---------------- MAIN CONTAINER ----------------
with st.container():

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    text = st.text_area(
        "✍ Enter Text",
        height=180,
        placeholder="Type something to translate..."
    )

    col1, col2 = st.columns(2)

    with col1:
        source_lang = st.selectbox(
            "🌐 From",
            list(languages.keys())
        )

    with col2:
        target_lang = st.selectbox(
            "🌍 To",
            list(languages.keys()),
            index=1
        )

    # ---------------- TRANSLATE BUTTON ----------------
    if st.button("🚀 Translate Now"):

        if text.strip() == "":
            st.warning("⚠ Please enter some text")

        else:
            try:

                translated = GoogleTranslator(
                    source=languages[source_lang],
                    target=languages[target_lang]
                ).translate(text)

                st.success("✅ Translation Successful")

                st.markdown(
                    f"""
                    <div class='output-box'>
                    <b>Translated Text:</b><br><br>
                    {translated}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # ---------------- TEXT TO SPEECH ----------------
                tts = gTTS(translated)
                tts.save("translation.mp3")

                audio_file = open("translation.mp3", "rb")
                audio_bytes = audio_file.read()

                st.audio(audio_bytes, format="audio/mp3")

                # ---------------- DOWNLOAD BUTTON ----------------
                st.download_button(
                    label="⬇ Download Translation",
                    data=translated,
                    file_name="translated_text.txt",
                    mime="text/plain"
                )

                # ---------------- HISTORY ----------------
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

            except Exception as e:
                st.error("❌ Translation Failed")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HISTORY SECTION ----------------
if "history" in st.session_state:

    st.markdown("## 🕓 Translation History")

    for item in reversed(st.session_state.history):

        st.markdown(f"""
        <div class='glass' style='margin-bottom:15px;'>
        ⏰ <b>{item['time']}</b><br><br>

        <b>Input:</b><br>
        {item['input']}<br><br>

        <b>Output:</b><br>
        {item['output']}
        </div>
        """, unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<br><br>
<center>
Made with ❤️ using Streamlit & AI
</center>
""", unsafe_allow_html=True)
