# Базовый образ python (облегчённый)
FROM python:3.12-slim
# Устанавливаем рабочую папку
WORKDIR /app
# Копируем requirements.txt
COPY requirements.txt ./
# Устанавливаем все зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Копируем всё приложение
COPY . .
# Открываем порт 8000
EXPOSE 8000
# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
