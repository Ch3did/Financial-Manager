from sqlalchemy.orm import sessionmaker

from src.env import engine


class Connection:
    def __init__(self):
        self.engine = engine

    def make_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session
