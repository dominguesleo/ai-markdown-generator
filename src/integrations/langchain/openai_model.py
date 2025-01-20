from langchain_openai import ChatOpenAI

from .base_model import BaseLangChainModel

class OpenAILangChainModel(BaseLangChainModel):
    def __init__(self, model_name: str, api_key: str, temperature: float, max_tokens: int):
        if not model_name:
            raise ValueError("No model name provided for OpenAI model.")
        if not api_key:
            raise ValueError("No API key provided for OpenAI model.")
        if not isinstance(temperature, (float, int)) or not (0 <= temperature <= 1):
            raise ValueError("Temperature must be a float between 0 and 1.")
        if not isinstance(max_tokens, int) or max_tokens <= 0:
            raise ValueError("Max tokens must be a positive integer.")
        
        super().__init__(model_name=model_name, temperature=temperature, max_tokens=max_tokens)
        self.api_key = api_key
        self.llm: ChatOpenAI = self.initialize_model()

    def initialize_model(self) -> ChatOpenAI:
        return ChatOpenAI(api_key=self.api_key, model=self.model_name, temperature=self.temperature)