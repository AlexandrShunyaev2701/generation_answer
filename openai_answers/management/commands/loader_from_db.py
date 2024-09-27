import json
from django.core.management import BaseCommand
from openai_answers.models import Answer

class Command(BaseCommand):
    help = 'Loader from database'

    def add_arguments(self, parser) -> None:
        parser.add_argument('file_path', type=str, help='The path to the file containing the project data')

    def handle(self, *args, **kwargs) -> None:
        file_path = kwargs['file_path']
        objects_list = []

        try:
            # Открываем и читаем весь файл как JSON-массив
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)  # Загрузка всего содержимого JSON-файла
                for entry in data:
                    obj = self.create_obj_answer(entry)
                    if obj:
                        objects_list.append(obj)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка чтения файла: {e}"))
            return

        if objects_list:
            Answer.objects.bulk_create(objects_list)
            self.stdout.write(self.style.SUCCESS(f"Успешно загружено {len(objects_list)} записей."))
        else:
            self.stdout.write(self.style.WARNING("Не найдено валидных записей для загрузки."))

    def create_obj_answer(self, data):
        """
        Извлекаем данные из словаря и формируем объект модели Answer
        """
        try:
            url = data.get('url')
            title = data.get('title')
            description = data.get('description')

            if not url or not title or not description:
                raise ValueError("Отсутствуют необходимые данные (url, title, description)")

            answer = Answer(
                url=url,
                title=title,
                description=description
            )
            return answer
        except (KeyError, ValueError, json.JSONDecodeError) as e:
            self.stdout.write(self.style.WARNING(f"Ошибка при парсинге записи: {e}"))
            return None
