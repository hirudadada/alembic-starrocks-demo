"""add user table

Revision ID: 002
Revises: 001
Create Date: 2024-12-12 12:28:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
    CREATE TABLE users (
        user_id BIGINT NOT NULL COMMENT "User ID",
        username VARCHAR(64) NOT NULL COMMENT "Username",
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Creation time",
        profile JSON COMMENT "User profile data"
    ) ENGINE=OLAP
    DUPLICATE KEY(user_id, username)
    DISTRIBUTED BY HASH(user_id) BUCKETS 8
    PROPERTIES (
        "replication_num" = "1"
    );
    """)


def downgrade():
    op.execute("DROP TABLE IF EXISTS users;")
