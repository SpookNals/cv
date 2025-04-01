import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def dip_or_cert(df, title):

    st.markdown(f"## {title}")

    # Create 3 columns
    cols = st.columns(3)

    # Loop through DataFrame rows
    for idx, row in df.iterrows():
        col = cols[idx % 3]  # Cycle through 0, 1, 2
        with col:
            st.markdown(f"#### {row['value']}")
            pdf_viewer(row['filepath'], width=400, height=500)