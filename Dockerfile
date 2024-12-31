FROM python:3.13-alpine

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    linux-headers \
    # Required for MySQL/StarRocks client
    mariadb-connector-c-dev \
    # Required for PostgreSQL client
    postgresql-dev

# Create appuser
RUN adduser -D -h /app appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

WORKDIR /app