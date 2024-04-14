import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from text_text.textfunction import content_creation, text_to_speech






def lang_translation():
    language_names = [
        "English", "Chinese", "Spanish", "French", "Russian", "Arabic", "Hindi", "Bengali",
        "Portuguese", "Urdu", "Indonesian", "German", "Japanese", "Swahili", "Telugu", "Marathi",
        "Tamil", "Turkish", "Vietnamese", "Korean", "Italian", "Filipino", "Thai", "Yoruba",
        "Malayalam", "Sindhi", "Punjabi", "Ukrainian", "Romanian", "Dutch", "Pashto", "Kannada",
        "Odia", "Malay", "Nepali", "Greek", "Hungarian", "Czech", "Bulgarian"
    ]

   
   
    st.title("Text to Translation")

    title_html = """
        <div style="background: linear-gradient(to right, #FFC600, #FD6E6A); -webkit-background-clip: text;
        -webkit-text-fill-color: transparent; font-size: 36px; font-weight: bold; padding: 10px;">
        Text to Translation
        </div>
        """
    st.markdown(title_html, unsafe_allow_html=True)

    prompt = st.text_input("Enter your prompt:")
    options = st.multiselect('Select languages', language_names)

    if st.button("Translate"):
        if not options:
                st.warning("Please select at least one language.")
        else:
            for lang in options:
                    translated_text = content_creation(lang, prompt)
                    audio_bytes = text_to_speech(translated_text, lang)
                    st.audio(audio_bytes, format="audio/mp3")
                    st.markdown(
                        f"""
                        <div class="card" style="background: linear-gradient(to right, #FFC600, #FD6E6A); 
                        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); border-radius: 10px; padding: 10px; margin: 10px;">
                        <h3 style="color: white;">{lang}</h3>
                        <p style="color: white;">Translated Text:</p>
                        <p>{translated_text}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

# Run the app
# lang_translation()
