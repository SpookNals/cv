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
    pdf_files = {
    "Senior general secondary education diploma": "dip_cert/Hoger algemeen voortgezet onderwijs - EN.pdf"
    }
    dip_or_cert(pdf_files=pdf_files, title="Diplomas")
        
with cert_tab:
    pdf_files = {
        "Creative Business Propedeutic": "dip_cert/HBO Bachelor Creative Business Propedeuse bachelor - EN.pdf",
        "ICT: Cyber Security Propedeutic": "dip_cert/HBO Bachelor HBO-ICT Propedeuse bachelor (Information & Communication Technology) - EN.pdf",
        "Dutch 3F Certificate": "dip_cert/Certificaat_3f_649308 (Taalkennis certificaat).pdf",
        "School der Poëzie Certificate": "dip_cert/Schoolofpoezie.pdf",
    }
    dip_or_cert(pdf_files=pdf_files, title="Certificates")