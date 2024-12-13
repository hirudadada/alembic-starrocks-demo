FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create appuser
RUN useradd -m -r appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

WORKDIR /app