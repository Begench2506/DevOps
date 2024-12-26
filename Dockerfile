# Используем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей (requirements.txt) в контейнер
COPY requirements.txt .

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Указываем, какой порт будет использовать приложение
EXPOSE 5000

# Указываем команду для запуска Flask-приложения
CMD ["python", "app.py"]
