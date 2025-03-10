from datetime import datetime

import click

from src.env import FOLDER_PATH
from src.views.category_view import CategoryView
from src.views.config import ConfigView
from src.views.transaction_view import TransactionsView


@click.group(help="Financial-Manager")
def config(): ...


# CONFIGURATION
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command("home", help="Print the home screen")
@click.option("-t", help="Specifies a type of search from Categories", default=1)
def home(t):
    ConfigView().make_homescreen(t)


@config.command("migrate", help="Run migrations")
def run_migrations():
    ConfigView().run_migrate()


# Transactions
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command("top", help="Return the first top transactions")
@click.argument("results", default="10", type=click.INT, required=False)
def top_transactions(results):
    TransactionsView().return_top_transactions(results)


@config.command("import", help="Imports an OFX")
@click.argument(
    "path",
    default=f"{FOLDER_PATH}/arquivo.ofx",
    type=click.Path(exists=True),
    required=False,
)
def update_transactions(path):
    TransactionsView().import_ofx(path)


@config.command("export", help="Export an CSV with all transactions")
@click.argument(
    "path",
    default=f"{FOLDER_PATH}output_{datetime.now().isoformat()[:10]}.csv",
    type=click.Path(exists=False),
    required=False,
)
def export_transactions(path):
    TransactionsView().export_csv(path)


# Category
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command("category", help="Get categories list")
def get_category_info():
    CategoryView().get_categories()


@config.command("create", help="Register a new category")
def create_category():
    CategoryView().new_category()


if __name__ == "__main__":
    config()
