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
        st.image(f"data:image/jpeg;base64,{img_base64}", width=600)

    with col2:
        # Parse date of birth
        dob_str = df['Date of Birth'].iloc[0]
        dob = datetime.strptime(dob_str, "%d %b %Y")

        # Calculate age
        today = datetime.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

        # Icons for fun ✨
        email_icon = "📧"
        phone_icon = "📞"
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
                st.markdown(f"{name_icon}  **Name:** {df['Name'].iloc[0]}")
                st.markdown(f"{email_icon} **E-mail:** {df['E-mail'].iloc[0]}")
                st.markdown(f"{phone_icon} **Phone:** {df['Phone Number'].iloc[0]}")                    

            with col4:
                st.markdown(f"{birth_icon} **Age:** {age}")
                st.markdown(f"{flag_icon} **Nationality:** Dutch")  # Hardcoded or auto-translated
                st.markdown(f"{license_icon} **Driving License:** {df['Driving License'].iloc[0]}")
                st.markdown(f"{language_icon} **Languages:** {df['Languages'].iloc[0]}")
            st.markdown("---")
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
                html(f"{folium_html}", height=350)
            else:
                st.markdown(f"{place_icon} **Place of Birth:** {place} (Map not found)")
    
    st.markdown("---")

    col5, col6 = st.columns(2)
    with col5:
        st.markdown("## Personality Traits")
        with st.container():
            st.markdown("---")
            col7, col8 = st.columns(2)
            with col7:
                for trait in traits[:len(traits)//2]:
                    st.markdown(f" - {trait}")
            with col8:
                for trait in traits[len(traits)//2:]:
                    st.markdown(f" - {trait}")

    with col6:
        me_jpeg = "photos/8766A0FD-D216-4799-88EC-48FC4D15F08F_1_105_c.jpeg"
        img_base64 = get_image_base64(me_jpeg)
        st.image(f"data:image/jpeg;base64,{img_base64}", width=600)
