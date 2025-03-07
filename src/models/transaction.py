from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel  # , PrivateAttr

from src.env import engine


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    description: str
    date: datetime
    value: float
    transaction_type: str
    transaction_id: str
    organization: str
    org_id: str
    account: str
    # _category_name: str = PrivateAttr()
    category_id: int | None

    def to_json(self, **kwargs):
        data = self.dict(**kwargs)
        data["change_timestamp"] = data["change_timestamp"].isoformat()
        if data["creation_date"] and isinstance(data["creation_date"], datetime):
            data["creation_date"] = data["creation_date"].isoformat()
        return data


def make_migrations():
    SQLModel.metadata.create_all(engine)
