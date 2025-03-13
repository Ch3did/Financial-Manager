from datetime import datetime

from sqlmodel import SQLModel

from src.controller.database import Database


class ConfigController(Database):

    def make_migrate(self):
        SQLModel.metadata.create_all(self.conn.engine)

    def get_transactions(
        self, start_date: datetime= None , end_date: datetime = datetime.now()
    ):
        if not start_date:
            start_date = end_date.replace(day=1)
            
        return self._get_transactions_with_range(start_date, end_date)
