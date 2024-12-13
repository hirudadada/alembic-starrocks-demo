import os
from logging.config import fileConfig
from urllib.parse import urlparse

from sqlalchemy import engine_from_config
from sqlalchemy import pool, text
from sqlalchemy import create_engine

from alembic import context
from starrocks import alembic

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Get database URL from environment with fallback
database_url = os.getenv("SQLALCHEMY_DATABASE_URI", "starrocks://root@dev.db:9030/test")

# StarRocks-specific configuration
engine_config = {
    "paramstyle": "named",
    "isolation_level": "AUTOCOMMIT",  # StarRocks requires AUTOCOMMIT
    "pool_pre_ping": True,  # Enable connection health checks
    "connect_args": {"charset": "utf8"}
}

# Override sqlalchemy.url with environment variable
config.set_main_option("sqlalchemy.url", database_url)

target_metadata = None

def get_engine():
    """Create SQLAlchemy engine with StarRocks configuration"""
    return create_engine(
        database_url,
        poolclass=pool.NullPool,
        **engine_config
    )

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        **engine_config
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            **engine_config
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
