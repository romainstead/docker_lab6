# Базовый образ python (облегчённый)
FROM python:3.12-slim
# Устанавливаем рабочую папку
WORKDIR /sub
# Копируем requirements.txt
COPY requirements.txt ./
# Устанавливаем все зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Копируем всё приложение
COPY . .
# Команда запуска приложения
CMD ["python", "main.py"]
