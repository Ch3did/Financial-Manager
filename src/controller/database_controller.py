import arrow
from loguru import logger
from sqlalchemy import and_

from src.helpers.connection import Connection
from src.helpers.exception import ATMException
from src.models.category import Category
from src.models.register import OFXRegister
from src.models.transaction import Transaction


class Database:
    def __init__(self):
        self.conn = Connection()

    def _add_debit(self, transaction):
        with self.conn.make_session()() as session:
            if not self.transaction_exists(transaction):
                session.add(transaction)
                logger.info(f"Inserido no OFXHandlero: {transaction['title']}")
                session.commit()

    def _transaction_exists(self, incomming_transaction):
        with self.conn.make_session()() as session:
            exists = (
                session.query(Transaction)
                .filter(
                    and_(
                        Transaction.checknum == incomming_transaction.checknum,
                        Transaction.detail == incomming_transaction.detail,
                        Transaction.date == incomming_transaction.date,
                        Transaction.establishment
                        == incomming_transaction.establishment,
                        Transaction.typename == incomming_transaction.typename,
                        Transaction.amount == incomming_transaction.amount,
                        Transaction.is_negative == incomming_transaction.is_negative,
                    )
                )
                .first()
            )
        return bool(exists)

    def _add_register(self, register: OFXRegister):
        with self.conn.make_session()() as session:
            session.add(register)
            logger.info(f"Inserido no OFXHandlero: {register['title']}")
            session.commit()

    def _get_transactions(self, limit: int = 10):
        with self.conn.make_session()() as session:
            return (
                session.query(Transaction, Category)
                .join(Category, Transaction.category == Category.id)
                .order_by(Transaction.date)
                .limit(limit)
                .all()
            )

    def _get_transactions_without_category(self):
        with self.conn.make_session()() as session:
            return (
                session.query(Transaction).filter(Transaction.category_id == None).all()
            )
