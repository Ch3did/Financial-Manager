from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from src.env import engine


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    description: str
    expected: float
    created_at: datetime
    updated_at: datetime

    transactions: List["Transaction"] = Relationship(back_populates="category")


def make_migrations():
    SQLModel.metadata.create_all(engine)
