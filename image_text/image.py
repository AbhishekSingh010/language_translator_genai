from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from image_text.imagefunc import get_gemini_response,input_image_setup





# Load environment variables
load_dotenv()

# Configure GenerativeAI API (replace with your actual API key)

# Define the Streamlit app
def run_image_to_text_translation():
    # st.set_page_config(page_title="Image to Text Translation")

    # Custom CSS for styling
    custom_css = """
    <style>
        .title {
            background: -webkit-linear-gradient(left, #ff8a00, #e52e71);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 36px;
            font-family: serif;
            text-align: center;
        }
        .response {
            background-color: #f4f4f4;
            border-radius: 10px;
            padding: 10px;
            margin-top: 20px;
            color: red;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 class='title'>Gemini Application</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Extract information from image and translate</h3>", unsafe_allow_html=True)

    # Input prompt and image upload
    language_names = [
        "English", "Chinese", "Spanish", "French", "Russian", "Arabic", "Hindi", "Bengali",
        "Portuguese", "Urdu", "Indonesian", "German", "Japanese", "Swahili", "Telugu", "Marathi",
        "Tamil", "Turkish", "Vietnamese", "Korean", "Italian", "Filipino", "Thai", "Yoruba",
        "Malayalam", "Sindhi", "Punjabi", "Ukrainian", "Romanian", "Dutch", "Pashto", "Kannada",
        "Odia", "Malay", "Nepali", "Greek", "Hungarian", "Czech", "Bulgarian"
    ]

    # Improved title formatting
    title_html = """
    <div style="background: linear-gradient(to right, #FFC600, #FD6E6A); -webkit-background-clip: text;
                 -webkit-text-fill-color: transparent; font-size: 36px; font-weight: bold; padding: 10px;">
        Text to Translation
    </div>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    input_prompt = """
    You are an expert in fetching text from the image.
    You will receive input images and perform the following actions with the extracted text:
    1. Show the extracted text.
    2. Translate the extracted text into the selected languages.
    """

    options = st.multiselect('Select languages', language_names)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Process extraction upon clicking the button
    if st.button("Translate"):
        if uploaded_file is None:
            st.error("Please upload an image.")
        else:
            try:
                image_data = input_image_setup(uploaded_file)

                with st.spinner("Processing..."):
                    # Display extracted text (optional)
                    # response =
                    # Display extracted text (optional)
                    # response = get_gemini_response(input_prompt, image_data, "Show the extracted text")
                    # if len(response.candidates) > 0 and hasattr(response.candidates[0], "content"):
                    #     extracted_text = response.candidates[0].content
                    #     st.subheader("Extracted Text:")
                    #     st.write(extracted_text)

                    for lang in options:
                        prompt = f"Translate the extracted text into {lang}."
                        # Add handling for potential translation errors
                        try:
                            response = get_gemini_response(input_prompt, image_data, prompt)
                            if len(response.candidates) > 0 and hasattr(response.candidates[0], "content"):
                                translated_text = response.candidates[0].content
                                st.subheader(f"{lang} Translated Text:")
                                st.markdown(f'<div class="response">{translated_text}</div>', unsafe_allow_html=True)
                            else:
                                st.error(f"No translation found for {lang}.")
                        except Exception as e:
                            st.error(f"An error occurred during {lang} translation: {e}")

            except Exception as e:
                st.error(f"An error occurred: {e}")

# # Run the app
# if __name__ == "__main__":
#     run_image_to_text_translation()
