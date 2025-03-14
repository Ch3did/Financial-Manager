from loguru import logger
from sqlalchemy import and_
from sqlalchemy.orm import joinedload, sessionmaker

from src.env import engine
from src.models.category import Category
from src.models.logs import Logs
from src.models.transaction import Transaction
from datetime import datetime


class Database:
    def __init__(self):
        self.engine = engine

    def make_session(self):
        Session = sessionmaker(bind=self.engine)
        return Session

    def _add_debit(self, transaction: Transaction) -> None:
        with self.make_session()() as session:
            if not self._transaction_exists(transaction):
                session.add(transaction)
                logger.debug(f"Inserida nova Transação: {transaction.description}")
                session.commit()

    def _add_log(self, log: Logs):
        with self.make_session()() as session:
            session.add(log)
            logger.debug("Inserido novo Registro de Importação")
            session.commit()

    def _add_category(self, category: Category):
        with self.make_session()() as session:
            if not self._category_exists(category):
                session.add(category)
                session.commit()

    def _category_exists(self, incomming_category: Category) -> bool:
        with self.make_session()() as session:
            exists = (
                session.query(Category)
                .filter(Category.name == incomming_category.name)
                .first()
            )
        return bool(exists)

    def _transaction_exists(self, incomming_transaction: Transaction) -> bool:
        with self.make_session()() as session:
            exists = (
                session.query(Transaction)
                .filter(
                    and_(
                        Transaction.description == incomming_transaction.description,
                        Transaction.date == incomming_transaction.date,
                        Transaction.value == incomming_transaction.value,
                        Transaction.transaction_type
                        == incomming_transaction.transaction_type,
                        Transaction.transaction_id
                        == incomming_transaction.transaction_id,
                        Transaction.organization == incomming_transaction.organization,
                        Transaction.org_id == incomming_transaction.org_id,
                        Transaction.account == incomming_transaction.account,
                    )
                )
                .first()
            )
        return bool(exists)

    def _get_transactions_with_limit(self, limit: int = 10, offset: int = 0):
        with self.make_session()() as session:
            return (
                session.query(Transaction)
                .options(joinedload(Transaction.category))
                .order_by(Transaction.date.desc())
                .limit(limit)
                .offset(offset)
                .all()
            )
            
    def _get_transactions_with_range(self, start_date: datetime, end_date: datetime):
        with self.make_session()() as session:
             return (
                session.query(Transaction)
                .options(joinedload(Transaction.category))
                .filter(Transaction.date >= start_date, Transaction.date <= end_date)
                .order_by(Transaction.date)
                .all()
            )

    def _get_transactions_without_category(self):
        with self.make_session()() as session:
            return (
                session.query(Transaction).filter(Transaction.category_id is None).all()
            )

    def _get_category_list(self):
        with self.make_session()() as session:
            return session.query(Category).order_by(Category.id).all()
