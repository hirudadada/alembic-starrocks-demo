"""create demo table

Revision ID: 001
Revises: 
Create Date: 2024-12-12 12:26:35.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create a demo table that shows StarRocks features
    op.execute("""
    CREATE TABLE demo_events (
        event_time DATETIME NOT NULL COMMENT "Event timestamp",
        event_type VARCHAR(32) NOT NULL COMMENT "Type of event",
        user_id BIGINT NOT NULL COMMENT "User ID",
        data JSON COMMENT "Event data in JSON format"
    ) ENGINE=OLAP
    DUPLICATE KEY(event_time, event_type, user_id)
    PARTITION BY RANGE(event_time) (
        PARTITION p20240101 VALUES LESS THAN ('2024-01-01 00:00:00'),
        PARTITION p20240201 VALUES LESS THAN ('2024-02-01 00:00:00'),
        PARTITION p20240301 VALUES LESS THAN ('2024-03-01 00:00:00')
    )
    DISTRIBUTED BY HASH(user_id) BUCKETS 8
    PROPERTIES (
        "replication_num" = "1",
        "dynamic_partition.enable" = "true",
        "dynamic_partition.time_unit" = "MONTH",
        "dynamic_partition.start" = "-2",
        "dynamic_partition.end" = "2",
        "dynamic_partition.prefix" = "p",
        "dynamic_partition.buckets" = "8"
    );
    """)


def downgrade():
    op.execute("DROP TABLE IF EXISTS demo_events;")
