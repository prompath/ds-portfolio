import sys

from dotenv import load_dotenv
import mariadb
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

from .credentials import (
    MARIADB_HOST,
    MARIADB_PASSWORD,
    MARIADB_PORT,
    MARIADB_USERNAME,
    MARIADB_DATABASE,
)

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
    engine = create_engine(
        f"mariadb+mariadbconnector://{MARIADB_USERNAME}:{MARIADB_PASSWORD}@{MARIADB_HOST}:{MARIADB_PORT}/{MARIADB_DATABASE}"
    )
    conn = engine.connect()
    return conn


class FinancialDBConnection:
    _accepted_connectors = ["mariadb", "sqlalchemy"]

    def __init__(self):
        self.conn_fn = None
        self.conn = None

    def _check_connection_exists(self):
        if self.conn_fn is None or self.conn is None:
            raise Exception("No connection found. Use `set_connection` first.")

    def set_connection(self, connector: str):
        if connector not in self._accepted_connectors:
            raise ValueError(
                f"Invalid connector. Accepted connectors are {self._accepted_connectors}"
            )

        if connector == "mariadb":
            conn_fn = get_mariadb_connection
        elif connector == "sqlalchemy":
            conn_fn = get_sqlalchemy_connection

        self.conn_fn = conn_fn
        self.conn = conn_fn()

    def query(self, sql: str) -> pd.DataFrame:
        self._check_connection_exists()
        try:
            result = pd.read_sql(sql, con=self.conn)
        except Exception as e:
            print(
                f"Query failed with exception: `{e}`. \nThe connection will be reinstantiated."
            )
            self.conn = self.conn_fn() # type: ignore
            result = pd.read_sql(sql, con=self.conn)
        return result
