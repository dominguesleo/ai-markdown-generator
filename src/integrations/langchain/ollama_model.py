from langchain_ollama import ChatOllama

from .base_model import BaseLangChainModel

class OllamaLangChainModel(BaseLangChainModel):
    def __init__(self, model_name:str, url:str, temperature:float, max_tokens:int):
        if not model_name:
            raise ValueError("No model name provided for Ollama model.")
        if not url:
            raise ValueError("No URL provided for Ollama model.")
        if not isinstance(temperature, (float, int)) or not (0 <= temperature <= 1):
            raise ValueError("Temperature must be a float between 0 and 1.")
        if not isinstance(max_tokens, int) or max_tokens <= 0:
            raise ValueError("Max tokens must be a positive integer.")
        super().__init__(model_name=model_name, temperature=temperature, max_tokens=max_tokens)

        self.url = url
        self.llm: ChatOllama = self.initialize_model()

    def initialize_model(self) -> ChatOllama:
        return ChatOllama(base_url=self.url, model=self.model_name, temperature=self.temperature)