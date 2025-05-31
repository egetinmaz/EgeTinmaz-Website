import streamlit as st

# Set page configuration
st.set_page_config(page_title="Contact",initial_sidebar_state="collapsed") 
margin_r,body,margin_l = st.columns([1, 2, 1])

#Header
st.title("Contact Me", divider="grey")

# Contact Details
st.markdown("""
- **Email**: egetinmaz@gmail.com
- **Phone**: +1 (650) 200-8293
- **LinkedIn**: www.linkedin.com/in/ege-tinmaz
- **GitHub**: https://github.com/egetinmaz
""")
