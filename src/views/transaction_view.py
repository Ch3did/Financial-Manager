from loguru import logger

from src.controller.category_controller import CategoryController
from src.controller.transactions_controller import TransactionController
from src.helpers import clean_output
from src.views.output import Output


class TransactionsView(Output):
    def __init__(self):
        super().__init__()
        self.transaction = TransactionController()
        self.category = CategoryController()

    @clean_output
    def import_ofx(self, path: str):
        try:
            self.transaction.import_file(path)

        except Exception as error:
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

        except Exception as error:
            logger.error(f"{error}")

    @clean_output
    def update_transaction(self, id):
        try:
            self._make_rodape("Update Category from Debit ")
            # data = self.category.get_categories_list()

            print("Changed sucessfully!")
        except Exception as error:
            logger.error(f"{error}")

    def complete_category_on_transactions(self):
        # category_list = self._get_category_list()
        for transaction in self.transaction.get_incomplete_transactions():
            self.update_category(transaction)
