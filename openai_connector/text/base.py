from abc import ABC, abstractmethod
from openai import OpenAI


class TextGenericGenerationBase(ABC):
    model: str = None
    openai_client: OpenAI = None
    messages: list = None
    user_content: str = None
    system_content: str = None
    max_tokens: int = None
    n: int = None
    stop: str = None
    temperature: float = None
    response: str = None

    @abstractmethod
    def generate_text(self):
        pass

    @abstractmethod
    def create_messages(self):
        pass
