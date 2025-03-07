import arrow
from loguru import logger
from tabulate import tabulate

from src.controller.category_controller import CategoryController
from src.controller.database_controller import Database
from src.controller.transactions_controller import TransactionController
from src.helpers import clean_output
from src.views.output import Output


class TransactionsView(Output):
    def __init__(self):
        self.transaction = TransactionController()

    @clean_output
    def import_ofx(self, path: str):
        try:
            self.transaction.import_file(path)

        except Exception as error:
            logger.error(error)

    @clean_output
    def return_top_transactions(self, period):
        self._make_rodape("Return Top Transactions")
        try:
            debit_list = [
                (
                    "id",
                    "establishment",
                    "date",
                    "typename",
                    "amount",
                    "description",
                    "category",
                )
            ]
            data = Pai().get_debits(period)
            for item in data:
                values = (
                    item[0].id,
                    item[0].establishment,
                    arrow.get(item[0].date).format("YYYY-MM-DD"),
                    item[0].typename,
                    f"{item[0].amount:,.2f}",
                    item[0].description,
                    item[1].name,
                )
                debit_list.append(values)

            print(tabulate(debit_list, headers="firstrow"))

        except Exception as error:
            logger.error(f"{error}")

    @clean_output
    def update_debit_category_view(self, id):
        self._make_rodape("Update Category from Debit ")
        try:
            data = CategoryController().get_categories_list(0)
            table = [("ID", "Name")]

            for item in data:
                lista = (item.id, item.name)
                table.append(lista)

            print(tabulate(table, headers="firstrow"))

            category_id = int(input(f"\nInput category_id for debit {id}?: "))

            Database().update_debits_category(id, category_id)

            print("Changed sucessfully!")
        except Exception as error:
            logger.error(f"{error}")

    # @clean_output(bypass_hit_enter=True)
    # def update_category(self, transaction: Transaction, category_list: List[Category]):
    #     self._make_rodape()
    #     self.transaction.update_transaction_category(transaction)
