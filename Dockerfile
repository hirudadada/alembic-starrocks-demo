FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && \
    useradd -m -r -u 1000 appuser

RUN pip install --no-cache-dir \
    alembic==1.14.0 \
    sqlalchemy==2.0.23 \
    psycopg2-binary==2.9.9 \
    pymysql==1.1.0 \
    starrocks==1.2.0

COPY alembic.ini ./

RUN alembic init migrations && \
    chown -R appuser:appuser /app

USER appuser

# VOLUME ["/app/migrations"]

CMD ["alembic", "--help"]