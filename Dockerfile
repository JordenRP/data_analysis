
# Используем официальный образ Python 3.10
FROM python:3.10-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем pip и обновляем его
RUN pip install --upgrade pip

# Устанавливаем зависимости проекта
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Создаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта в рабочую директорию
COPY . /app

# Указываем команду по умолчанию
ENTRYPOINT ["python"]
