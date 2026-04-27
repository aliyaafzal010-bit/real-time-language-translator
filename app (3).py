import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="AI Translator", page_icon="🌍")

st.title("🌍 AI Language Translator")
st.write("Translate text instantly using AI 🚀")

translator = Translator()

text = st.text_area("Enter text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

col1, col2 = st.columns(2)

with col1:
    src = st.selectbox("From", list(languages.keys()))

with col2:
    dest = st.selectbox("To", list(languages.keys()))

if st.button("Translate"):
    if text:
        result = translator.translate(text, src=languages[src], dest=languages[dest])
        st.success(result.text)
    else:
        st.warning("Enter text first")
