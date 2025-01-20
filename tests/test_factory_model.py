import os
import pytest
from unittest.mock import patch
from src.integrations.langchain.factory_model import LangChainModelFactory
from src.integrations.langchain.ollama_model import OllamaLangChainModel
from src.integrations.langchain.openai_model import OpenAILangChainModel

def test_create_model_ollama():
    with patch.dict(os.environ, {
        "PROVIDER": "ollama",
        "OLLAMA_MODEL": "test_model",
        "OLLAMA_URL": "http://test.url",
        "TEMPERATURE": "0.5",
        "MAX_OUTPUT_TOKENS": "500"
    }):
        model = LangChainModelFactory.create_model()
        assert isinstance(model, OllamaLangChainModel)
        assert model.model_name == "test_model"
        assert model.url == "http://test.url"
        assert model.temperature == 0.5
        assert model.max_tokens == 500

def test_create_model_openai():
    with patch.dict(os.environ, {
        "PROVIDER": "openai",
        "OPENAI_API_KEY": "test_api_key",
        "OPENAI_MODEL": "test_model",
        "TEMPERATURE": "0.6",
        "MAX_OUTPUT_TOKENS": "600"
    }):
        model = LangChainModelFactory.create_model()
        assert isinstance(model, OpenAILangChainModel)
        assert model.api_key == "test_api_key"
        assert model.temperature == 0.6
        assert model.max_tokens == 600

def test_create_model_invalid_provider():
    with patch.dict(os.environ, {
        "PROVIDER": "invalid_provider"
    }):
        with pytest.raises(ValueError, match="Invalid provider: invalid_provider"):
            LangChainModelFactory.create_model()