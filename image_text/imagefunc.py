from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image




load_dotenv()

api_key=os.environ.get('GOOGLE_API_KEY')



def image_to_text(image):
 
# Load environment variables
   load_dotenv()

# Configure GenerativeAI API
   genai.configure(api_key=api_key)

# Function to get Gemini response
   def get_gemini_response(input_prompt, image_data, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input_prompt, image_data[0], prompt])
    return response.text



genai.configure(api_key=api_key)

# Function to get Gemini response
def get_gemini_response(input_prompt, image_data, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input_prompt, image_data[0], prompt])
    return response

# Function to load image details
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {"mime_type": uploaded_file.type, "data": bytes_data}
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
