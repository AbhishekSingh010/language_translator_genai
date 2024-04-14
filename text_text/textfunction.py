import streamlit as st
from dotenv import load_dotenv
import os  # Import the os module here
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

# from function import content_creation

# Load environment variables
load_dotenv()

api_key=os.environ.get('GOOGLE_API_KEY')






def content_creation(lang, topic):
    if lang is None or topic is None:
        return "Please select a language and enter a topic."
    
    load_dotenv()  # Assuming you're using dotenv to load environment variables
    api_key = os.environ.get('GOOGLE_API_KEY')
    
    if api_key is None:
        raise ValueError("Google API key not found in environment variables")
    
    tweet_prompt = PromptTemplate.from_template(f"""
                                                if translation not possible give sentence not possible in english  
Translate the word '{topic}' into {lang}. use any cultural or regional meanings if present. For complex languages like Tamil, Telugu, Greek, Hungarian, Czech, and Bulgarian, 
give one formal translation. For other languages, provide  formal  translations if applicable if not then informal .
Prioritize formal translations for languages like Russian, Ukrainian, Romanian, Czech, and Bulgarian.""")

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)
    response = tweet_chain.run(topic=topic)
    
    return response

    





# Function to convert text to speech using gTTS without saving to file
def text_to_speech(text, lang):
    
    # Language codes for Google Text-to-Speech (gTTS)
    language_codes = {
    "English": "en","Chinese": "zh","Spanish": "es", "French": "fr","Russian": "ru",
    "Arabic": "ar","Hindi": "hi", "Bengali": "bn", "Portuguese": "pt",
    "Urdu": "ur","Indonesian": "id","German": "de","Japanese": "ja",
    "Swahili": "sw","Telugu": "te","Marathi": "mr","Tamil": "ta","Turkish": "tr",
    "Vietnamese": "vi","Korean": "ko","Italian": "it","Filipino": "fil","Thai": "th","Yoruba": "yo",
    "Malayalam": "ml","Sindhi": "sd","Punjabi": "pa","Ukrainian": "uk","Romanian": "ro",
    "Dutch": "nl","Pashto": "ps","Kannada": "kn","Odia": "or","Malay": "ms",
    "Nepali": "ne", "Sinhala": "si", "Greek": "el", "Hungarian": "hu", "Czech": "cs",
    "Bulgarian": "bg"
}


    # Get the language code from the dictionary
    language_code = language_codes.get(lang)
    if not language_code:
        st.error("Language not supported.")
        return
    else:
    # Create a gTTS object and generate speech
      tts = gTTS(text=text, lang=language_code)
      audio_bytes = BytesIO()
      tts.write_to_fp(audio_bytes)
      audio_bytes.seek(0)
      
      return audio_bytes
    #   return audio_bytes
  
  





#  return=>lang,text
