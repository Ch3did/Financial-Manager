from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from src.env import engine


class Categories(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    description: str
    expected: float
    created_at: datetime
    updated_at: datetime
    is_visible: bool
    # TODO: Add key-words


def make_migrations():
    SQLModel.metadata.create_all(engine)
