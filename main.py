import streamlit as st
from streamlit_option_menu import option_menu

from homepage import sidebar
from text_text import texttrans
from homepage import home 
from image_text import image






css = """
    <style>
        body {
            background-color: #006375;
            font-family: 'Arial', sans-serif;
            background-image: url('stocks2.jfif');
            background-size: cover;
            margin-top : 0px ;
        }
        .stApp {
            max-width: 1500px;
            margin: 0 auto;
            margin-top : 0px;
        }
        .st-h1 {
            color: #333333;
            text-align: center;
        }
        .btn-primary {
                color: #fff;
                background-color: #007bff;
                border-color: #007bff;
        }
    </style>
"""
st.markdown(css, unsafe_allow_html=True)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    
    @staticmethod
    def run():
        sidebar.sidebar()
        st.title("Language Translation App 🌐")
        app = option_menu(
            menu_title="",
            options=["Homepage", "Language Translation", "image text translation"],
            icons=["house-fill", "book-fill", "stack-overflow"],
            default_index=0,
            orientation="horizontal"
        )

        if app == "Homepage":
            home.home()
        elif app == "Language Translation":
            texttrans.lang_translation()
        elif app == "image text translation":
            image.run_image_to_text_translation()
        # elif app == "data finder":
        #     home.finder()

# Run the app
MultiApp.run()
