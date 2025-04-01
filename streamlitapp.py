import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objects as go
import plotly.express as px
import base64
from datetime import datetime
from tabs.persona import persona
from tabs.skills import skills
from tabs.work import work
from tabs.education import education
from tabs.dip_or_cert import dip_or_cert
from streamlit_pdf_viewer import pdf_viewer


st.set_page_config(
    page_title="Curriculum Vitae",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded",
)

# title
st.title("Curriculum Vitae")

p_tab, skill_tab, edu_tab, cert_tab, dip_tab, work_tab= st.tabs(
    ["Persona","Skills","Education", "Certificates", "Diplomas", "Work Experience"]
    )

with p_tab:
    persona()

with skill_tab:
    skills()

with work_tab:
    work()

with edu_tab:
    education()

with dip_tab:
    df = pd.read_csv("data/certificates_and_diplomas.csv")
    df_cert = df[df["type"] == "diploma"]

    dip_or_cert(df=df_cert, title="Diplomas")
        
with cert_tab:
    df = pd.read_csv("data/certificates_and_diplomas.csv")
    df_cert = df[df["type"] == "certificate"]

    dip_or_cert(df=df_cert, title="Certificates")