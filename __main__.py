import streamlit as st
from dotenv import load_dotenv


st.set_page_config(
    page_title="MD Generator",
    page_icon="🤖",
    layout="wide",
)

def main():
    load_dotenv()
    st.title("🏠 AI Markdown Generator")
    st.write(
        """
        This application is an assistant that facilitates the conversion of content
        from various text sources into Markdown format. It also includes an intelligent
        assistant that enables real-time Markdown editing.
        """
    )

    st.subheader("📋 Available Formats:")
    st.markdown(
        """
        - **PDF**
        - **PowerPoint**
        - **Word**
        - **Excel**
        - **HTML**
        - **Text-based formats**: CSV, JSON, XML
        """
    )
    st.write("Note: Unexpected behavior may occur when including images with text within the document. It is recommended to manually review the document in such cases.")

pg = st.navigation([
    st.Page(main, title="Home", icon="🏠"),
    st.Page("src/pages/generator.py", title="MD Generator", icon="🤖"),
])

pg.run()