import os
from markitdown import MarkItDown
from typing import Any, Optional

class MarkdownConverter:
    def __init__(self, uploaded_file: Optional[Any] = None):
        self.temp_file_path: Optional[str] = None
        self.uploaded_file: Optional[Any] = uploaded_file
        self.markdown_converter: MarkItDown = MarkItDown()

    def _save_uploaded_file(self) -> str:
        if self.uploaded_file is None:
            raise ValueError("No uploaded file to save.")

        self.temp_file_path = self.uploaded_file.name
        with open(self.temp_file_path, "wb") as temp_file:
            temp_file.write(self.uploaded_file.read())
        return self.temp_file_path

    def _convert_file(self) -> str:
        try:
            markdown_output = self.markdown_converter.convert(self.temp_file_path)
            return markdown_output.text_content
        except Exception as e:
            raise RuntimeError(f"Error processing file with MarkItDown: {e}")
        finally:
            self._cleanup()

    def _cleanup(self) -> None:
        if self.temp_file_path and os.path.exists(self.temp_file_path):
            os.remove(self.temp_file_path)

    def file_to_markdown(self, uploaded_file: Optional[Any] = None) -> str:
        if uploaded_file is not None:
            self.uploaded_file = uploaded_file
        if self.uploaded_file is None:
            raise ValueError("No uploaded file provided.")

        self._save_uploaded_file()
        return self._convert_file()
    
