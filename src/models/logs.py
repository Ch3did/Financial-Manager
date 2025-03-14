from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel

from src.env import engine


class Logs(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    org_id: str
    account: str
    start_date: datetime
    end_date: datetime
    organization: str
    amount: float



def make_migrations():
    SQLModel.metadata.create_all(engine)
