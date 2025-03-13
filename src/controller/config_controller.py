from sqlmodel import SQLModel

from datetime import datetime
from src.controller.database import Database


class ConfigController(Database):

    def make_migrate(self):
        SQLModel.metadata.create_all(self.conn.engine)

    def get_transactions(self, start_date: datetime = datetime.now(), end_date: datetime = 0):
        return self._get_transactions_with_limit()
