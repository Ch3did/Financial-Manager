from loguru import logger

from src.controller.transactions_controller import TransactionController
from src.helpers import clean_output
from src.views.output import Output
from src.helpers.exception import ExtractionException, InputException


class TransactionsView(Output):
    def __init__(self):
        super().__init__()
        self.transaction = TransactionController()

    @clean_output
    def import_ofx(self, path: str):
        try:
            self.transaction.import_file(path)
            logger.info("Import Sucessfully")
        except InputException as error:
            logger.error(error)

    @clean_output
    def export_csv(self, path: str):
        try:
            self.transaction.export_file(path)
            logger.info("Export Sucessfully")
        except ExtractionException as error:
            logger.error(error)

    @clean_output
    def return_top_transactions(self, limit):
        try:
            self._make_rodape("Return Top Transactions")
            transaction_data = self.transaction.get_transactions(limit)
            # # category_data = self.category.get_category()
            # for transaction in transaction_data:
            #     transaction

            self.return_tabulated_data(transaction_data)

        except ExtractionException as error:
            logger.error(f"{error}")

    @clean_output
    def update_transaction(self, id):
        try:
            self._make_rodape("Update Category from Debit ")
            # data = self.category.get_categories_list()

            print("Changed sucessfully!")
        except InputException as error:
            logger.error(f"{error}")

    def complete_category_on_transactions(self):
        try:
            category_list = self.transaction._get_category_list()
            for transaction in self.transaction.get_incomplete_transactions():
                self.update_category(transaction)
        except InputException as err:
            logger.error(f"{error}")