import streamlit as st

def sidebar():
   

# Define the CSS styles for the sidebar card and gradient text
  sidebar_css = """
<style>
.sidebar-card {
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
}

.gradient-text {
    background: -webkit-linear-gradient(#ff8a00, #e52e71);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 24px;
    font-weight: bold;
}
</style>
"""



# Define the CSS for the sidebar
#   sidebar_style = """
#     background-color: #f0f0f0;
#     padding: 20px;
#     border-radius: 10px;
#     box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
# """

# Define the CSS for the Gen AI text
  gen_ai_style = """
    font-size: 70px;
    font-weight: bold;
    background-image: linear-gradient(to bottom, #4CAF50, #008CBA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
"""

# Add the sidebar content
  st.sidebar.markdown(
    f"""
   
        <div style="{gen_ai_style}">
            G<br>
            e<br>
            n<br><br>
            A<br>
            I<br>
        </div>
    
    """,
    unsafe_allow_html=True,
)
#  <div style="{sidebar_style}">
# </div>

# Display the sidebar with the styled card and gradient text
  st.sidebar.markdown(sidebar_css, unsafe_allow_html=True)
  with st.sidebar.container():
    st.markdown('<div class="sidebar-card"><img src="https://icon-library.com/images/bot-icon/bot-icon-10.jpg" width="100"/><h1 class="gradient-text">Gen Ai</h1></div>', unsafe_allow_html=True)

    
    
    