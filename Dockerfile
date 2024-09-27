FROM python:3.11-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /answer_project

# Копируем файл зависимостей в контейнер
COPY req.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r req.txt

# Копируем все файлы в рабочую директорию контейнера
COPY . .

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]