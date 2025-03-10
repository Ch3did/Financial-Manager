from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.env import engine
from src.models.category import Category


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
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")

    category: Optional[Category] = Relationship(back_populates="transactions")

    def to_json(self, **kwargs):
        data = self.dict(**kwargs)
        data["change_timestamp"] = data["change_timestamp"].isoformat()
        if data["creation_date"] and isinstance(data["creation_date"], datetime):
            data["creation_date"] = data["creation_date"].isoformat()
        return data


def make_migrations():
    SQLModel.metadata.create_all(engine)
