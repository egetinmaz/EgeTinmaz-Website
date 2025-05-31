import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Home",initial_sidebar_state="collapsed") 
margin_r,body,margin_l = st.columns([1, 2, 1])

st.sidebar.success("Select a page above.")

# Home Page Header
st.header("A Little About Me:", divider="grey")

# Intro and Image
col1, col2, col3 = st.columns([1.3, 0.2, 1])

with col1:
    st.markdown("Name: Ege Tinmaz")
    st.markdown("Current Position: Technical Support Analyst")
    st.markdown("Company: Odoo")
    st.markdown("Location: San Mateo, California")
    st.markdown("Education: University of San Francisco, B.A. in Psychology")
    st.markdown("Linkedin: www.linkedin.com/in/ege-tinmaz")
    st.markdown("Github: https://github.com/egetinmaz")
    
    with open("src/Resume.pdf", "rb") as file:
        resume = file.read()

    st.download_button(
        label="Download Resume",
        data=resume,
        file_name="Resume.pdf",
        mime="application/pdf")

with col3:
    st.image("src/portrait.jpg", width=360)

# Summary Section
st.markdown("""
## Summary
Highly organized and accomplished professional with strong collaboration, customer support, and technical background. 
""")

# Skills Section
st.markdown("""
## Skills
- **Python Programming**: Proficient in Python for data analysis and web development.
- **SQL Queries**: Use sliders, buttons, and text inputs and testing.
- **AWS**: Display charts and graphs.
- **Markdown Support**: Write formatted text with Markdown. 
""")

# Certificates Section
st.markdown("""
## Certificates
- **Python**: Testing and debugging Python applications.
- **SQL**: Use sliders, buttons, and text inputs and testing.
- **AWS**: Display charts and graphs.            
""")
