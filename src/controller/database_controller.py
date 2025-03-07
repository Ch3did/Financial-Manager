from loguru import logger
from sqlalchemy import and_

from src.helpers.connection import Connection
from src.models.category import Category
from src.models.register import OFXRegister
from src.models.transaction import Transaction


class Database:
    def __init__(self):
        self.conn = Connection()

    def _add_debit(self, transaction: Transaction) -> None:
        with self.conn.make_session()() as session:
            if not self._transaction_exists(transaction):
                session.add(transaction)
                logger.debug(f"Inserida nova Transação: {transaction.description}")
                session.commit()

    def _add_register(self, register: OFXRegister):
        with self.conn.make_session()() as session:
            session.add(register)
            logger.debug("Inserido novo Registro de Importação")
            session.commit()

    def _add_category(self, category: Category):
        with self.conn.make_session()() as session:
            if not self._category_exists(category):
                session.add(category)
                session.commit()

    def _category_exists(self, incomming_category: Category) -> bool:
        with self.conn.make_session()() as session:
            exists = (
                session.query(Category)
                .filter((Category.name == incomming_category))
                .first()
            )
        return bool(exists)

    def _transaction_exists(self, incomming_transaction: Transaction) -> bool:
        with self.conn.make_session()() as session:
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

    def _get_transactions_with_limit(self, limit: int = 10):
        with self.conn.make_session()() as session:
            return (
                session.query(Transaction).order_by(Transaction.date).limit(limit).all()
            )

    def _get_transactions_without_category(self):
        with self.conn.make_session()() as session:
            return (
                session.query(Transaction).filter(Transaction.category_id is None).all()
            )

    def _get_category_list(self):
        with self.conn.make_session()() as session:
            return session.query(Category).all()
