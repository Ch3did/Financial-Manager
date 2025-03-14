from datetime import datetime
from typing import List

from src.controller.database import Database
from src.models.register import Register


class RegisterController(Database):

    def create_register(self, data: dict) -> Register:
        register = Register(
            name=data["name"],
            sentense=data["sentence"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            category_id=data["category"],
        )
        self._add_register(register)
