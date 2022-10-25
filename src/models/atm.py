import arrow
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from src.get_env import SCHEMA

from ..helpers.database import Database

metadata_obj = MetaData(schema=SCHEMA)

Base = declarative_base(metadata=metadata_obj)


class Bills(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    amount = Column(Numeric, nullable=False)
    instalments = Column(Integer, nullable=False, default=1)
    due_instalment = Column(Numeric, nullable=False)
    start_date = Column(DateTime, nullable=False, default=arrow.now())
    end_date = Column(DateTime, nullable=True)
    payment_day = Column(String(2), nullable=True, default="01")
    description = Column(Text, nullable=False)
    use = Column(Boolean, nullable=False, default=True)
    categories_id = Column(Integer, ForeignKey("categories.id"))


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    description = Column(Text, nullable=True)
    expected = Column(Numeric, nullable=True)
    liquid = Column(Numeric)
    created_at = Column(
        DateTime, default=arrow.now().strftime("%Y-%m-%d")
    )  # Data da primeira vez que foi usado
    updated_at = Column(
        DateTime, default=arrow.now().strftime("%Y-%m-%d")
    )  # Data que foi alterado
    is_visible = Column(Boolean, default=True)
    # TODO: Add key-words
    statment = relationship("Statment")
    bills = relationship("Bills")


class Statment(Base):
    __tablename__ = "statments"
    id = Column(Integer, primary_key=True)
    checknum = Column(String(100), nullable=False)
    detail = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    typename = Column(String(100), nullable=False)
    amount = Column(Numeric, nullable=False)
    # ForeignKey
    statment_type_id = Column(Integer, ForeignKey("statment_types.id"))
    categories_id = Column(Integer, ForeignKey("categories.id"))
    establishment_id = Column(Integer, ForeignKey("establishments.id"))


class Establishments(Base):
    __tablename__ = "establishments"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    created_at = Column(
        DateTime, default=arrow.now().strftime("%Y-%m-%d")
    )  # Data da primeira vez que foi usado
    updated_at = Column(
        DateTime, default=arrow.now().strftime("%Y-%m-%d")
    )  # Data que foi alterado
    detail = Column(Text, nullable=True)
    address = Column(String(60), nullable=True)
    statment = relationship("Statment")
    is_visible = Column(Boolean, default=True)
    is_pf = Column(Boolean, default=False)

    # TODO: added Typo de estabelecimento


class StatmentTypes(Base):
    __tablename__ = "statment_types"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    description = Column(Text, nullable=True)
    is_math_use = Column(Boolean, default=False)
    is_negative = Column(Boolean)
    statment = relationship("Statment")


def bank_raiser():
    try:
        engine = Database().engine
        Base.metadata.create_all(engine)
        return True
    except Exception as error:
        return False
