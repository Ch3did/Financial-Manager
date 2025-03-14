from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from src.env import engine
from src.models.category import Category

class Register(SQLModel, table=True):
    # São Palavras que devo procurar na descrição do ofx e
    # que podem me ajudar a categorizar
    id: Optional[int] = Field(default=None, primary_key=True)
    sentense: str
    start_date: datetime
    end_date: datetime

    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="register", sa_relationship_kwargs={"uselist": False})  # 1:1 relacionamento
    

def make_migrations():
    SQLModel.metadata.create_all(engine)
