#!/bin/bash

# docker compose down -v
docker compose up --build -d
# docker compose up -d setup.db
# docker compose up -d dev.db
# sleep 30  # wait for starrocks to be ready
# docker compose up alembic 