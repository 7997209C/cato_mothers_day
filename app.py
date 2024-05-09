import streamlit as st
from streamlit_extras.let_it_rain import rain
import random

# Let flowers rain
def flower1():
    rain(
        emoji="🏵️",
        font_size=60,
        falling_speed=5,
        animation_length="infinite"
    )
 
def flower2():
    rain(
        emoji="🌷",
        font_size=60,
        falling_speed=5,
        animation_length="infinite"
    )
def flower3():
    rain(
        emoji="🪷",
        font_size=60,
        falling_speed=5,
        animation_length="infinite"
    )

# Set page title and layout
st.set_page_config(page_title="Mother's Day Card", layout="centered")

# Random messages for Mother's Day
messages = [
    "Roses are red, Violets Are Blue, you are awesome and i love you too",
    "You Are The Best Mom In The World!!!!",
    "You Mean So Much To Me!",
    "I Love You So Much!!!",
    "Happy Mother's Day to the most amazing mom!"
]

# Select a random message
random_message = random.choice(messages)

# Create a container to hold the card
card = st.container()

# Apply styles to the card
card.markdown(
    """
    <style>
        .card {
            border: 2px solid black;
            padding: 20px;
            border-radius: 15px;
            background-color: #FF6347; /* Red color */
            color: white;
            font-family: 'Arial';
            box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
            text-align: center;
            margin: 50px auto;
            width: 400px;
        }
        h1{
            color:white;
        }
        [data-testid="stButton"] {
            width: 250px; /* Adjust button width */
            height: 100px; /* Adjust button height */
            font-size: 24px; /* Adjust font size */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the card with a random message
with card:
    st.markdown(f"""
    <div class='card'>
        <h2>🌷 Happy Mother's Day! 🌷</h2>
        <h1>{random_message}</h1>
    </div>
    """, unsafe_allow_html=True)

col = st.columns(5,gap="small")
with col[1]:
    f1 = st.button("🏵️", key="rain")
with col[2]:
    f2 = st.button("🌷", key="rain2")
with col[3]:
    f3 = st.button("🪷", key="f3")
    
if f1==True:
    flower1()
if f2 == True:
    flower2()
if f3 == True:
    flower3()
