import streamlit as st

# Sidebar for navigation
with st.sidebar:
    st.success("Select a page above.")

# Home Page Content
st.header("Welcome to My Streamlit App", divider="rainbow")
st.subheader("This is a simple example of a Streamlit application.")

col1, col2, col3 = st.columns([1.5, 0.3, 1.3])

with col1:
    st.markdown ("Name: Ege Tinmaz")
    st.markdown("Current Position: Technical Support Analyst")
    st.markdown("Company: Odoo")
    st.markdown("Interest:")
    st.markdown("Favorite Color: Yellow")
    st.markdown("Linkedin: www.linkedin.com/in/ege-tinmaz")
    
with col3:
    st.image("https://via.placeholder.com/200", use_container_width=True)

st.markdown("""
## Summary
Highly organized and accomplished professional with strong collaboration, customer support, and technical background. 
""")

st.markdown("""
## Skills
- **Python Programming**: Proficient in Python for data analysis and web development.
- **SQL Queries**: Use sliders, buttons, and text inputs and testing.
- **AWS**: Display charts and graphs.
- **Markdown Support**: Write formatted text with Markdown. 
""")

st.markdown("""
## Certificates
- **Python**: Testing and debugging Python applications.
- **SQL**: Use sliders, buttons, and text inputs and testing.
- **AWS**: Display charts and graphs.            
""")