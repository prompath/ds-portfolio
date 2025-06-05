import sys

from dotenv import load_dotenv
import mariadb

from .credentials import MARIADB_HOST, MARIADB_PASSWORD, MARIADB_PORT, MARIADB_USERNAME

load_dotenv()

def get_db_connection() -> mariadb.Connection:
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(
            user=MARIADB_USERNAME,
            password=MARIADB_PASSWORD,
            host=MARIADB_HOST,
            port=MARIADB_PORT,
            database="financial",
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn
