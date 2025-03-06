from sqlmodel import Field, SQLModel

from src.env import engine

from ..helpers.connection import Connection


class Config:
    def __init__(self):
        self.conn = Connection()
        
    def make_migrate(self):
        SQLModel.metadata.create_all(self.conn.engine)
        self.conn.commit()
        self.conn.close()
