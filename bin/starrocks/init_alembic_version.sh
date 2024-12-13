#!/bin/bash

db_host="127.0.0.1"

if [ -n "$DB_HOST" ]; then
    db_host="$DB_HOST"
fi

db_name=${DB_NAME}

SQL_STMT=$(cat << END_SQL
USE \`${db_name}\`;

CREATE TABLE IF NOT EXISTS alembic_version (
    version_num VARCHAR(32) NOT NULL
)
ENGINE=PRIMARY
PRIMARY KEY(version_num)
DISTRIBUTED BY HASH(version_num)
PROPERTIES (
    "replication_num" = "1",
    "storage_format" = "DEFAULT"
);
END_SQL
)

mysql -P 9030 -h ${db_host} -u root -e "$SQL_STMT"

echo "Alembic version table is created."
