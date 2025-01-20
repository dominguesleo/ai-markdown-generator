import pytest
from unittest.mock import Mock, patch
from src.integrations.markitdown import MarkdownConverter

def test_file_to_markdown_no_uploaded_file():
    converter = MarkdownConverter()
    with pytest.raises(ValueError, match="No uploaded file provided."):
        converter.file_to_markdown()

def test_file_to_markdown_with_uploaded_file():
    mock_file = Mock()
    mock_file.name = "test.md"
    mock_file.read.return_value = b"Some content"

    converter = MarkdownConverter()
    with patch.object(converter, '_save_uploaded_file', return_value="test.md") as mock_save, \
         patch.object(converter, '_convert_file', return_value="Converted content") as mock_convert:
        result = converter.file_to_markdown(mock_file)
        mock_save.assert_called_once()
        mock_convert.assert_called_once()
        assert result == "Converted content"

def test_file_to_markdown_with_existing_uploaded_file():
    mock_file = Mock()
    mock_file.name = "test.md"
    mock_file.read.return_value = b"Some content"

    converter = MarkdownConverter(uploaded_file=mock_file)
    with patch.object(converter, '_save_uploaded_file', return_value="test.md") as mock_save, \
         patch.object(converter, '_convert_file', return_value="Converted content") as mock_convert:
        result = converter.file_to_markdown()
        mock_save.assert_called_once()
        mock_convert.assert_called_once()
        assert result == "Converted content"