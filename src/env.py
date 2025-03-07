import os

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv("monetary_maid.config")

# Basics
DEBUG = os.environ.get("DEBUG")

# Nubank Data
FOLDER_PATH = os.environ.get("FOLDER_PATH")

# DB Conection
DB_NAME = os.environ.get("DB_NAME")
DATABASE_URL = f"sqlite:///{DB_NAME}.db"


engine = create_engine(DATABASE_URL, echo=bool(DEBUG))
