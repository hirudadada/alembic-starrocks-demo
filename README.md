# StarRocks Alembic Migration Tool (PoC)

A Docker-based database migration tool for StarRocks using Alembic.

## Project Structure 

```plaintext
.
├── Dockerfile # Python environment with Alembic
├── docker-compose.yml # Services: StarRocks DB and Alembic
├── alembic.ini # Alembic configuration
├── migrations/ # Migration scripts
│ ├── versions/ # Version files
│ ├── env.py # Environment configuration
│ └── script.py.mako # Migration template
├── start.sh # Startup script
├── setup.sh # Initial setup script
├── .env # Environment variables
└── .dockerignore # Docker build exclusions
```

## Quick Start

1. Setup environment:
```bash
# Create .env file with database connection
SQLALCHEMY_DATABASE_URI=starrocks://root@dev.db:9030/demo
```

2. Start services:

```bash
chmod +x start.sh
./start.sh
```

## Services

- **dev.db**: StarRocks database (port 9030)
- **setup.db**: Database initialization service
- **alembic**: Migration service

## Creating Migrations

Create a new migration:
```bash
docker compose run --rm alembic revision -m "create_table"
```

Example migration:
```python
def upgrade() -> None:
  op.execute('''
    CREATE TABLE demo.test (
      id INT NOT NULL,
      name VARCHAR(255)
    ) ENGINE = OLAP
      DUPLICATE KEY(id)
    ''')
def downgrade() -> None:
  op.execute('DROP TABLE demo.test')
```


## Configuration

### Docker Volumes
- `./migrations:/app/migrations:rw`: Migration scripts

### Environment Variables
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `DB_NAME`: Database name for StarRocks

## Notes

- Uses MySQL protocol for StarRocks compatibility (changed to use Starrocks's 
adapter on November 2024)
- Supports StarRocks-specific DDL (OLAP engine, DUPLICATE KEY, etc.)
- Waits for database initialization before running migrations

## Dependencies

- StarRocks 3.3.7
- Python 3.9
- Alembic 1.14.1
- SQLAlchemy 2.0.23
- PyMySQL 1.1.0
- StarRocks-Python-Connector 1.1.0

## License

MIT
