import openai
from django.conf import settings
from openai_connector.text.generic import TextGenerationGeneric


class AnswerTextGenerator(TextGenerationGeneric):
    openai_client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
    model = "gpt-4"
    max_tokens = 3000
    n = 1
    stop = None
    system_content = ("Ты представитель IT компании Eora, я буду задавать тебе вопросы, "
                      "что бы ты мог на них ответить, я передам тебе url ссылки на проекты, их заголовки и краткое описание. "
                      "Ответ должен так же содержать ссылки на те проеткы о которых ты говоришь. Вот пример вопроса и твоего ответа на него: "
                      "- Что вы можете сделать для ритейлеров?"
                      "- Например, мы делали бота для HR для Магнита 'https://eora.ru/cases/chat-boty/hr-bot-dlya-magnit-kotoriy-priglashaet-na-sobesedovanie', а ещё поиск по "
                      "картинкам для KazanExpress 'https://eora.ru/cases/kazanexpress-poisk-tovarov-po-foto'"
                      "Только не присылай выдуманных ссылок, используй только тот материал что я тебе передал")
    temperature = 0.7

    def __init__(self, combined_content: str, user_question: str):
        self.user_content = (f"combined_content: {combined_content}"
                             f"User question: {user_question}"
                             )
