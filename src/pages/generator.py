import streamlit as st

from src.integrations.markitdown import MarkdownConverter
from src.integrations.langchain.factory_model import LangChainModelFactory

st.title("🤖 AI Markdown Generator")

uploaded_file = st.sidebar.file_uploader("Upload your file", type=["pdf", "pptx", "docx", "xlsx", "html", "csv", "json", "xml"])

@st.cache_data
def process_file(uploaded_file):
    model = LangChainModelFactory.create_model()
    converter = MarkdownConverter()
    markdown_content = converter.file_to_markdown(uploaded_file)
    optimized_markdown = model.optimize_markdown(markdown_content)
    return markdown_content, optimized_markdown

if uploaded_file is None:
    st.write("Please upload a file to generate Markdown content.")
else:
    with st.spinner("Processing..."):
        try:
            markdown_content, optimized_markdown = process_file(uploaded_file)

            tab1, tab2, tab3, tab4 = st.tabs(["MD Optimized", "MD Optimized (raw)", "Extracted text", "Extracted text (raw)"])
            with tab1:
                st.markdown(optimized_markdown, unsafe_allow_html=True)
            with tab2:
                st.code(optimized_markdown, language="markdown")
            with tab3:
                st.markdown(markdown_content, unsafe_allow_html=True)
            with tab4:
                st.code(markdown_content, language="markdown")

            st.sidebar.download_button(
                label="Download Optimized Markdown",
                data=optimized_markdown,
                file_name=uploaded_file.name.split(".")[0] + "_optimized.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"Error processing file: {e}")

