from abc import ABC, abstractmethod
from typing import Optional
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.utils.prompt_utils import read_prompt_from_file

class BaseLangChainModel(ABC):
    def __init__(self, model_name:str, temperature:float, max_tokens:int):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.llm = None

    @abstractmethod
    def initialize_model(self) -> None:
        raise NotImplementedError("This method must be implemented by the subclass.")

    def optimize_markdown(self, markdown: str, template:Optional[str]=None) -> str:
        if self.llm is None:
            raise ValueError("No language model initialized.")

        if not markdown or not isinstance(markdown, str):
            raise ValueError("Markdown must be a non-empty string.")

        if template is None:
            try:
                template = read_prompt_from_file(r"src/templates/optimize_markdown_prompt.txt")
            except FileNotFoundError:
                raise ValueError("Default prompt file not found.")
            except Exception as e:
                raise ValueError(f"An error occurred while loading the default prompt: {e}")

        if not template.strip():
            raise ValueError("Loaded template is empty or invalid.")

        prompt_template = PromptTemplate(input_variables=["{input_text}"], template=template)
        chain = prompt_template | self.llm | StrOutputParser()

        try:
            result = chain.invoke(input={"input_text": markdown})
        except Exception as e:
            raise ValueError(f"An error occurred during markdown optimization: {e}")

        return result