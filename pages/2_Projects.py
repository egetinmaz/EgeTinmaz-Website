import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Projects",initial_sidebar_state="collapsed") 
margin_r,body,margin_l = st.columns([1, 2, 1])

# Add header
st.title("Projects")
st.header("Python:", divider="grey")

# Library Management System Project
st.markdown("""
## Library Management System
- Description of the project.""")
components.iframe("https://library-management-ege.streamlit.app?embed=true", height=450, width=800)
st.link_button("GitHub", "https://github.com/egetinmaz/Library-Management/tree/main", use_container_width=True)

# PDF-Text-To-Audio-Converter
st.markdown("""
## PDF-Text-To-Audio-Converter
- Description of the project.""")
components.iframe("https://pdf-text-to-audio-converter.streamlit.app?embed=true", height=450, width=800)
st.link_button("GitHub", "https://github.com/egetinmaz/PDF-Text-To-Audio-Converter/tree/main", use_container_width=True)
