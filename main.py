import arrow
import click

from src.views.categories import CategoryView
from src.views.config import ConfigView
from src.views.transaction import TransactionsView


@click.group(help="Configuration options")
def config(): ...


# CONFIGURATION
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command("home", help="Print the home screen")
@click.option("-t", help="Specifies a type of search from Categories", default=1)
def home(t):
    ConfigView.make_homescreen(t)


@config.command("migrate", help="Run migrations")
def run_migrations():
    ConfigView.run_migrate()


# Transactions
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command("top", help="Return the first top transactions")
@click.option(
    "--results",
    "-r",
    help="Number os results for the output",
    default="10",
)
def top_transactions(results):
    TransactionsView.return_top_transactions(results)


@config.command("import", help="Imports an OFX")
def update_transactions():
    TransactionsView.import_ofx()


# Category
#     ___     ___     ___     ___     ___     ___     ___     ___     ___
@config.command(help="Get categories list")
def get_category_info():
    CategoryView.get_categories()


@config.command("create", help="Register a new category")
def create_category():
    CategoryView.create_category()


if __name__ == "__main__":
    config()
