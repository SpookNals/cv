import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def dip_or_cert(pdf_files:dict[str,str], title:str):

    st.markdown(f"## {title}")

    # Create 3 columns
    cols = st.columns(3)

    # Loop through the PDFs and assign to columns
    for idx, (title, path) in enumerate(pdf_files.items()):
        col = cols[idx % 3]  # Cycle through 0, 1, 2
        with col:
            st.markdown(f"#### {title}")
            pdf_viewer(path, width=400, height=500)