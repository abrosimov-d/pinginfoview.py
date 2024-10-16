# Используем официальный базовый образ Python
FROM python:3.9-slim

# Установим обновления и необходимые пакеты
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Установим необходимые Python зависимости
RUN pip install --no-cache-dir ping3 seaborn

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем ваш скрипт в контейнер
COPY your_script.py .

# Укажем команду для запуска скрипта при старте контейнера
CMD ["python", "your_script.py"]
