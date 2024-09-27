# Это проект по генерации ответов на вопросы, опираясь на историю проектов компании Eora с использованием openAI
## Возможности приложения:
### - Парсинг данных о проектах с сайта Eora
### - Перенос спарсенных данных из файла output.json в БД
### - API в которой реализована возможность обращений с вопросом к openAI, где будут получены ответы опираясь на базу проктов компании Eora

## Установка, запуск проекта и работа с данными
### 1. Клонирование репозитория
    git clone ...
    cd <папка с проектом>

### 2. Настройка виртуальной среды

    python -m venv .venv
    source .venv/bin/activate

### 3. Конфигурация переменных окружения

    Создайте файл .env по примеру .env.example
### 4. Запуск проекта с помощью Docker

    docker-compose up --build

### 5. Миграции базы данных

    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate

### 6. Парсинг логов

Выполните вход в контейнер с приложением Django и выполните комманду:

    docker-compose exec web python manage.py start_for_parser
После парсинга в каталоге появится файл output.json с данными
Данный файл со всем содержимым уже есть в проекте для демонстрации

### 7. Перенос данных в БД
Выполните вход в контейнер с приложением Django и выполните комманду:

    docker-compose exec web python manage.py loader_from_db <укажите путь к файлу output.json>

## Работа с API
После запуска проекта перейдите по адресу http://localhost:8000/swagger/

И нужно воспользоваться endpoint /generator/generation_answer/

Передать в 
{
  "user_question": "Свой вопрос?"
}

И дождаться ответа от open AI

# ВАЖНО:
## Для работы с парсером необходимо использовать браузер Mazilla, а так же потребуется установить geckodriver
## Для работы с API понадобится VPN и OPENAI_API_KEY