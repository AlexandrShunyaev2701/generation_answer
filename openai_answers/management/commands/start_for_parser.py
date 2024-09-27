import json
import os
from django.core.management import BaseCommand
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from openai_answers.parser.urls_list import urls_list


class Command(BaseCommand):
    """
    Парсим необходимые данные о проектах с сайта eora.ru в файл openai_answers/parser/output.txt
    """
    help = 'Start the parser'

    def handle(self, *args, **kwargs) -> None:
        urls = urls_list
        # Указываем путь к geckodriver
        service = Service(os.environ.get('absolut_path_geckodriver'))

        # Запускаем Firefox
        driver = webdriver.Firefox(service=service)
        data = []
        for url in urls:
            driver.get(url)
            try:
                # Извлечение текста из <title>
                title = driver.execute_script("return document.title;")

                # Извлечение значения из <meta property="og:description">
                meta_description = driver.find_element(By.XPATH, "//meta[@property='og:description']").get_attribute(
                    "content")

                projects_data = {
                    "url": url,
                    "title": title,
                    "description": meta_description,
                }
                data.append(projects_data)
            except Exception as e:
                print(f"Ошибка для {url}: {e}")
        output_file_path = os.path.join('answer_project/openai_answers/parser', 'output.txt')
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        # Закрываем браузер
        driver.quit()
