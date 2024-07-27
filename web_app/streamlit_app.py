import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(page_title="Quantum - Alpha", page_icon=":satellite:", layout="centered")

# Load images
background_image = Image.open("background.jpg")
input_image_icon = "input_image_icon.png"
storage_icon = "storage_icon.png"
model_details_icon = "model_details_icon.png"
feedback_icon = "feedback_icon.png"
instagram_icon = "instagram_icon.png"
facebook_icon = "facebook_icon.png"
twitter_icon = "twitter_icon.png"

# CSS to style the page
st.markdown(
    f"""
    <style>
    body {{
        background-image: url('data:image/png;base64,{background_image}'); 
        background-size: cover;
        color: white;
        text-align: center;
    }}
    .container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        background: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
    }}
    h1 {{
        font-size: 3em;
        margin-bottom: 0;
    }}
    h2 {{
        font-size: 1.5em;
        margin-top: 0;
    }}
    .features {{
        display: flex;
        justify-content: space-around;
        width: 100%;
        max-width: 800px;
    }}
    .feature {{
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        width: 150px;
        text-align: center;
    }}
    .feature img {{
        width: 50px;
        height: 50px;
    }}
    .social-icons {{
        margin-top: 20px;
    }}
    .social-icons img {{
        width: 30px;
        height: 30px;
        margin: 0 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Main container
st.markdown("<div class='container'>", unsafe_allow_html=True)
st.markdown("<h1>Quantum - Alpha</h1>", unsafe_allow_html=True)
st.markdown("<h2>Feature Extraction from Remote Sensing Data using AI/ML</h2>", unsafe_allow_html=True)

# Features section
st.markdown("<div class='features'>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class='feature'>
        <img src='{input_image_icon}' alt='Input Image'>
        <p>INPUT Image</p>
    </div>
    <div class='feature'>
        <img src='{storage_icon}' alt='Storage'>
        <p>Storage</p>
    </div>
    <div class='feature'>
        <img src='{model_details_icon}' alt='Model Details'>
        <p>Model Details</p>
    </div>
    <div class='feature'>
        <img src='{feedback_icon}' alt='Feedback'>
        <p>Feedback</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

# Social icons section
st.markdown("<div class='social-icons'>", unsafe_allow_html=True)
st.markdown(
    f"""
    <a href="#"><img src='{instagram_icon}' alt='Instagram'></a>
    <a href="#"><img src='{facebook_icon}' alt='Facebook'></a>
    <a href="#"><img src='{twitter_icon}' alt='Twitter'></a>
    """,
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
