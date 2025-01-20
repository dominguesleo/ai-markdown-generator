import os

from .ollama_model import OllamaLangChainModel
from .openai_model import OpenAILangChainModel

class LangChainModelFactory:
    @staticmethod
    def create_model():
        provider = os.getenv("PROVIDER")
        temperature = float(os.getenv("TEMPERATURE", 0.7))
        max_tokens = int(os.getenv("MAX_OUTPUT_TOKENS", 4000))
        if provider == "ollama":
            return OllamaLangChainModel(
                model_name=os.getenv("OLLAMA_MODEL"),
                url=os.getenv("OLLAMA_URL"),
                temperature=temperature,
                max_tokens=max_tokens
            )
        elif provider == "openai":
            return OpenAILangChainModel(
                model_name=os.getenv("OPENAI_MODEL"),
                api_key=os.getenv("OPENAI_API_KEY"),
                temperature=temperature,
                max_tokens=max_tokens
            )
        else:
            raise ValueError(f"Invalid provider: {provider}")