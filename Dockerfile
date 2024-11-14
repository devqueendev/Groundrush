FROM python:3.12-slim
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    python3-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirments/production.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app

RUN chmod +x /app/entrypoint.sh

EXPOSE $APP_PORT


