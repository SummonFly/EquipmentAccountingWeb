# Use official slim image
FROM python:3.12-slim

# Install system deps (если нужны)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только нужные файлы и ставим зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект (папка Equipment_accounting_system уже внутри WORKDIR)
COPY . .

# 1. Выполняем миграции
RUN python Equipment_accounting_system/manage.py migrate --noinput

# 2. Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
