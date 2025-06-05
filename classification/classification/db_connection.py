import sys

from dotenv import load_dotenv
import mariadb
import sqlalchemy
from sqlalchemy import create_engine

from .credentials import MARIADB_HOST, MARIADB_PASSWORD, MARIADB_PORT, MARIADB_USERNAME, MARIADB_DATABASE

load_dotenv()

def get_mariadb_connection() -> mariadb.Connection:
    """Creates a connection using MariaDB Python connector.

    Returns:
        mariadb.Connection: MariaDB connection.
    """
    try:
        conn = mariadb.connect(
            user=MARIADB_USERNAME,
            password=MARIADB_PASSWORD,
            host=MARIADB_HOST,
            port=MARIADB_PORT,
            database=MARIADB_DATABASE,
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


def get_sqlalchemy_connection() -> sqlalchemy.Connection:
    """Creates a connection to MariaDB using SQLAlchemy.

    Returns:
        sqlalchemy.Connection: SQLAlchemy connection.
    """
    engine = create_engine(f"mariadb+mariadbconnector://{MARIADB_USERNAME}:{MARIADB_PASSWORD}@{MARIADB_HOST}:{MARIADB_PORT}/{MARIADB_DATABASE}")
    conn = engine.connect()
    return conn