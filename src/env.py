import os

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv("monetary_maid.config")

# Basics
DEBUG = os.environ.get("DEBUG")

# Nubank Data
FOLDER_PATH = os.environ.get("FOLDER_PATH")

USER_NAME = ""
# DB Conection
DB_NAME = os.environ.get("DB_NAME")
# DB_USER = os.environ.get("DB_USER")
# DB_PASSWORD = os.environ.get("DB_PASSWORD")
# DB_HOST = os.environ.get("DB_HOST")
# DB_PORT = os.environ.get("DB_PORT")

DATABASE_URL = f"sqlite:///{DB_NAME}.db"


engine = create_engine(DATABASE_URL, echo=bool(DEBUG))
