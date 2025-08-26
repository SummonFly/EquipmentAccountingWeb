# Базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочий каталог
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Собираем статические файлы (если нужно)
RUN python manage.py collectstatic --noinput

# Порт, который слушает Gunicorn
EXPOSE 8000

# Команда запуска
CMD ["gunicorn", "Equipment_accounting_system/Equipment_accounting_system.wsgi:app",
     "--bind", "0.0.0.0:8000",
     "--workers", "3"]
