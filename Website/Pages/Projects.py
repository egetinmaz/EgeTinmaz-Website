import streamlit as st
import streamlit.components.v1 as components

# Add header
st.header("Projects:", divider="grey")

# Library Management System Project
st.markdown("""
## Library Management System
- Description of the project.""")
components.iframe("https://library-management-ege.streamlit.app?embed=true", height=450, width=800)
st.link_button("GitHub", "https://github.com/egetinmaz/Library-Management/tree/main", use_container_width=True)
