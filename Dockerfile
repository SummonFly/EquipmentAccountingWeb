# Base image
FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=Equipment_accounting_system.settings

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Run migrations and start server
CMD ["gunicorn", "Equipment_accounting_system.wsgi:application",
     "--bind", "0.0.0.0:8000", "--workers", "1"]
