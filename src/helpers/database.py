from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.env import engine


class Database:
    def __init__(self):
        self.engine = engine
        self.session = self.make_session()

    def make_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session
