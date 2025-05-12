# translation_app.py

# Import necessary libraries
import streamlit as st
from googletrans import Translator

# Define supported languages
languages = {
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Bengali": "bn",
    "Gujarati": "gu",
    "Marathi": "mr",
    "Telugu": "te",
    "Hindi": "hi"
}

# Function to translate the phrase
def translate_phrase(phrase, target_language):
    try:
        # Initialize the translator
        translator = Translator()

        # Get the language code
        target_code = languages[target_language]

        # Translate the phrase
        translation = translator.translate(phrase, dest=target_code)

        return translation.text

    except Exception as e:
        return f"Translation failed: {str(e)}"

# Streamlit app
def main():
    st.set_page_config(page_title="Text Translation", page_icon="🌍", layout="centered")
    st.header("Text Translation 🌍")

    # Input field for text prompt
    text_prompt = st.text_input("Enter your text prompt here")

    # Select target language
    target_language = st.selectbox("Select target language", list(languages.keys()))

    # Translate button
    translate_button = st.button("Translate")

    # Display translated text
    if translate_button and text_prompt:
        with st.spinner("Translating..."):
            translated_text = translate_phrase(text_prompt, target_language)
        st.success(f"Translated '{text_prompt}' to {target_language}:")
        st.write(translated_text)

if __name__ == "__main__":
    main()
