import os

from dotenv import load_dotenv

load_dotenv()

MARIADB_HOST = os.environ["MARIADB_HOST"]
MARIADB_PORT = int(os.environ["MARIADB_PORT"])
MARIADB_USERNAME = os.environ["MARIADB_USERNAME"]
MARIADB_PASSWORD = os.environ["MARIADB_PASSWORD"]
MARIADB_DATABASE = os.environ["MARIADB_DATABASE"]
