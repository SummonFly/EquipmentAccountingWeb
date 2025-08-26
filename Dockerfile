# Use official slim image
FROM python:3.12-slim

# Install system deps (если нужны)
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только нужные файлы
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY Equipment_accounting_system ./Equipment_accounting_system

# Указываем точку входа (можно оставить в compose)
CMD ["python", "Equipment_accounting_system/manage.py", "runserver", "0.0.0.0:8000"]
