FROM  python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-client \
    postgresql-dev \
    && rm -rf /var/cache/apk/*
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

# Don't create appuser if it causes permission issues with volumes
# RUN useradd -m -u 1000 appuser && \
#     chown -R appuser:appuser /app
# USER appuser

RUN mkdir -p /app/staticfiles

EXPOSE 8000