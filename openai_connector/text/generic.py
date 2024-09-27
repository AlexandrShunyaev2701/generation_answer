from typing import List
import openai
from openai import OpenAI
from rest_framework.exceptions import ValidationError

from openai_connector.text.base import TextGenericGenerationBase


class TextGenerationGeneric(TextGenericGenerationBase):
    @classmethod
    def get_model(cls) -> str:
        assert cls.model is not None, (f"{cls.__name__}: model attribute must not be None or"
                                       f"override the get_model() method.")
        assert isinstance(cls.model, str), f"{cls.__name__}: model attribute must be a string"
        return cls.model

    @classmethod
    def get_system_content(cls) -> str:
        assert cls.system_content is not None, (f"{cls.__name__}: system_content attribute must not be None or"
                                       f"override the get_system_content() method.")
        assert isinstance(cls.system_content, str), f"{cls.__name__}: system_content attribute must be a string"
        return cls.system_content

    @classmethod
    def get_openai_client(cls) -> OpenAI:
        assert cls.openai_client is not None, (f"{cls.__name__}: openai_client attribute must not be None or"
                                               f"override the get_openai_client() method.")
        assert isinstance(cls.openai_client, OpenAI), f"{cls.__name__}: openai_client must be an OpenAI client."
        return cls.openai_client

    @classmethod
    def get_messages(cls) -> List[str]:
        assert cls.messages is not None, (f"{cls.__name__}: openai_client attribute must not be None or"
                                               f"override the get_openai_client() method.")
        assert isinstance(cls.messages, List), f"{cls.__name__}: openai_client must be an OpenAI client."
        return cls.messages

    def create_messages(self):
        messages = [
            {"role": "system", "content": self.system_content},
            {"role": "user", "content": self.user_content},
        ]
        return messages

    def generate_text(self):
        try:
            response = self.openai_client.chat.completions.create(
                model=self.model,
                messages=self.create_messages(),
                max_tokens=self.max_tokens,  # Допустимая длина генерируемого текста
                n=self.n,  # Генерация n вариаций текста
                stop=self.stop,
                temperature=self.temperature,  # Управляет уровнем креативности
            )
        except openai.OpenAIError as e:
            raise ValidationError(f"Error in text generation: {e}")

            # Извлечение текста из ответа через атрибут choices
        variations = [choice.message.content.strip() for choice in response.choices]
        return variations
