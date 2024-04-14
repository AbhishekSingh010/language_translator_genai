import streamlit as st

def home():
# Create a sidebar navigation bar
  # st.sidebar.title("Navigation")
  # page = st.sidebar.radio("Go to", ["Home", "Speech Translation"])

# Define functions for different pages
  def show_home_page():
    st.markdown("## Welcome to the Home Page")
    st.write("This is the home page content.")

  # def show_speech_translation_page():
  #   st.markdown("## Speech Translation")
    # Include your speech translation interface here

# Display the selected page based on navigation
  # if page == "Home":
  #   show_home_page()
  # elif page == "Speech Translation":
  #   show_speech_translation_page()


# Page Title with Background Image
  st.markdown(
    """
    <style>
        .title-text {
            font-size: 48px;
            font-weight: bold;
            color: #FFFFFF;
            background-image: linear-gradient(to right, #FD6E6A, #FFC600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding: 20px;
            font-family: 'Roboto', sans-serif;
        }
        .background-image_1 {
            background-image: url('https://cdn0.iconfinder.com/data/icons/translation/513/translation-translate-language_2_copy_11-256.png');
            background-size: cover;
            background-position: center;
            height: 600px;
        }
        .gradient-heading {
            background-image: linear-gradient(to right, #FFC600, #FD6E6A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Montserrat', sans-serif;
            font-size: 24px;
            padding: 10px 0;
        }
        .custom-card {
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            background-color: #F5F5F5; /* Greyish or matte white background */
            text-align: center;
        }
        .tool-card {
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            background-image: linear-gradient(to right, #6495ED, #FFC0CB);
            color: #FFFFFF;
            font-weight: bold;
            text-align: center;
        }
    </style>
    <div class="background-image_1">
        <p class="title-text">Vachnasarathi: Bridging the Language Gap with AI</p>
    </div>
    """,
    unsafe_allow_html=True,
)
    # st.markdown('<div class="sidebar-card"><img src="https://icon-library.com/images/bot-icon/bot-icon-10.jpg" width="100"/><h1 class="gradient-text">Gen Ai</h1></div>', unsafe_allow_html=True)
#

# Main Content
  st.markdown(
    """
    ## Imagine a world where language is no longer a barrier.

    With Vachnasarathi, a powerful language translation
    tool built on cutting-edge AI, clear communication across
    cultures and borders becomes a reality.
    """
)

# Cards for Tools
  col1, col2, col3 = st.columns(3)

# Language Translator Tool
  with col1:
    st.markdown("<p class='gradient-heading'>Language Translator</p>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'>Translate text between multiple languages and give voice output.<br><br><img src='https://cdn3.iconfinder.com/data/icons/network-communication-flat/48/Translator-512.png' width='100' height='100'></div>", unsafe_allow_html=True)

# Image Language Translator Tool
  with col2:
    st.markdown("<p class='gradient-heading'>Image text Translator</p>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'>Extract text from images and translate it.<br><br><img src='https://cdn3.iconfinder.com/data/icons/network-communication-flat/48/Translator-512.png' width='100' height='100'></div>", unsafe_allow_html=True)

# Speech Assistant Tool
  with col3:
    st.markdown("<p class='gradient-heading'>Data finder Assistant</p>", unsafe_allow_html=True)
    st.markdown("<div class='tool-card'>find the data from website give you leverage to ask question on that.<br><br><img src='https://cdn3.iconfinder.com/data/icons/network-communication-flat/48/Translator-512.png' width='100' height='100'></div>", unsafe_allow_html=True)

# Professional Content
  st.markdown(
    """
    ### Why Choose Vachnasarathi?

    - Cutting-edge AI technology for accurate translations.
    - User-friendly interface for seamless communication.
    - Support for multiple languages and diverse use cases.
    - Fast and efficient tools to save time and improve productivity.

    """
  )
    
    
  st.markdown(
    """
    <style>
        .background-image {
            background-image: url('https://mspoweruser.com/wp-content/uploads/2023/12/Google-Gemini-AI-model.jpg');
            background-size: cover;
            background-position: center;
            height: 600px;
        }
        .title-text {
            font-size: 48px;
            font-weight: bold;
            color: #FFFFFF;
            background-image: linear-gradient(to right, #FD6E6A, #FFC600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            padding: 20px;
            font-family: 'Roboto', sans-serif;
        }
    </style>
    <div class="background-image">
        <p class="title-text">What it uses behind?</p>
    </div>
    """,
    unsafe_allow_html=True
)
  st.markdown("""
                - it uses gemini Modale
                - it leverage the power of gemini pro and pro vision models
                - trained on billions of parameter 
              
              """
  
    
    
  )

# Footer
  st.markdown("---")
  st.write("© 2024 Vachnasarathi. All rights reserved.")
