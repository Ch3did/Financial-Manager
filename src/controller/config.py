from sqlmodel import Field, SQLModel

from src.env import engine
from src.models.categories import Categories

from ..helpers.database import Database



class Config:
    def __init__(self):
        db = Database()
        self.conn = db.session()
        self.engine = db.engine

    def make_migrate(self):
        SQLModel.metadata.create_all(engine)

        self.conn.commit()
        self.conn.close()
