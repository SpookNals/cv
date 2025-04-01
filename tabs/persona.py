import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objects as go
import plotly.express as px
import base64
from datetime import datetime
import folium
from geopy.geocoders import Nominatim
from streamlit.components.v1 import html
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_image_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
def persona():
    df = pd.read_csv("data/persona.csv")
    me_jpeg = "photos/C9049D6F-0DBC-4BE5-AF4C-58286D7A4A1F_1_105_c.jpeg"
    img_base64 = get_image_base64(me_jpeg)

    traits = df['Traits'].str.split(";").iloc[0] 

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_base64}" width="400" style="border-radius: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        # Parse date of birth
        dob_str = df['Date of Birth'].iloc[0]
        dob = datetime.strptime(dob_str, "%d %b %Y")

        # Calculate age
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Icons for fun ✨
        email_icon = "📧"
        birth_icon = "🎂"
        place_icon = "📍"
        flag_icon = "🏳️"
        license_icon = "🚗"
        language_icon = "🗣️"
        name_icon = "👤"

        # Card-style layout
        st.markdown("## Persona")

        with st.container():
            st.markdown("---")

            col3, col4 = st.columns(2)

            with col3:
                st.markdown(f"""
            <div class="compact-text">
                {name_icon} <b>Name:</b> {df['Name'].iloc[0]}<br>
                {email_icon} <b>E-mail:</b> {df['E-mail'].iloc[0]}<br>
                {birth_icon} <b>Age:</b> {age}<br>
            </div>
            """, unsafe_allow_html=True)
            with col4:
                st.markdown(f"""
            <div class="compact-text">
                {flag_icon} <b>Nationality:</b> {df['Nationality'].iloc[0]}<br>
                {language_icon} <b>Languages:</b> {df['Languages'].iloc[0]}<br>
                {license_icon} <b>Driving License:</b> {df['Driving License'].iloc[0]}
                </div>
            """, unsafe_allow_html=True)
            # Geocode place of birth
            st.markdown(f"{place_icon} **Place of Birth:** {df['Place of Birth'].iloc[0]}")
            place = df['Place of Birth'].iloc[0]
            geolocator = Nominatim(user_agent="myCV")
            location = geolocator.geocode(place)

            if location:
                m = folium.Map(location=[location.latitude, location.longitude], zoom_start=10)
                folium.Marker([location.latitude, location.longitude], popup=place).add_to(m)
                
                # Render folium map in Streamlit
                folium_html = m._repr_html_()
                html(f"{folium_html}", height=200)
            else:
                st.markdown(f"{place_icon} **Place of Birth:** {place} (Map not found)")
    
    st.markdown("---")
    st.markdown("## ✨ Personality Traits")

    # Turn list into string
    text = ' '.join(traits)

    # Create word cloud image
    wordcloud = WordCloud(
        width=1200,
        height=400,
        background_color='white',
        colormap='plasma',
        prefer_horizontal=1.0
    ).generate(text)

    # Display in Streamlit
    fig, ax = plt.subplots(figsize=(12, 4), dpi=150)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig, use_container_width=True)


    
    st.markdown("---")
    col5, col6 = st.columns(2)
    with col5:
        me_jpeg = "photos/8766A0FD-D216-4799-88EC-48FC4D15F08F_1_105_c.jpeg"
        img_base64 = get_image_base64(me_jpeg)

        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_base64}" width="400" style="border-radius: 20px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with col6:
        st.markdown("## 📜 About Me")
        st.write("""               
Good morning, afternoon, evening or night!

I am Niels and I am loaded with creativity and empathy. I can get lost in the world of entertainment and computers, and I am determined to keep my future Trudy-free (yes, we all know those Trudys, right?). The great thing is that I also have a passion for acquiring new knowledge in the field of ICT, where so far I have mostly gained theoretical knowledge. Fortunately, I have already completed several projects using SCRUM and Waterfall methods. For example, I built a Capture the Flag website where multiple challenges had to be overcome (for both the user and myself). I loved creating it and was incredibly proud of the result.

As for my personality, I can say that I am very loyal. I always give my full 100% and expect the same from others

        """)
