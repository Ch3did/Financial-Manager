import sys

from loguru import logger

from src.controller.category_controller import CategoryController
from src.controller.config_controller import Config
from src.controller.database_controller import Database
from src.helpers.clear import clean_output


class ConfigView:
    @clean_output
    def run_migrate(self):
        try:
            Config().make_migrate()
            logger.info("Tables Ready")

        except Exception as error:
            logger.error(f"Tables are Down... {error}")

    @clean_output
    def make_homescreen(self, search_type):
        try:
            categories = CategoryController().get_categories_list(search_type)
            transactions = Database().get_debits()
            plot_relation = {}
            for values in transactions:
                if values[1].name not in plot_relation:
                    plot_relation[values[1].name] = 0
                plot_relation[values[1].name] += values[0].amount
            print(
                "-------------------------------------------------------------------------------\n"
            )
            for item in categories:
                if item.is_spend:
                    bar_len = 45
                    count = abs(plot_relation.get(item.name, 0))
                    total = abs(item.expected)
                    title = item.name.title()
                    if total > count:
                        filled_len = int(round(bar_len * float(count) / float(total)))
                        bar = "#" * filled_len + "-" * (bar_len - filled_len)
                    else:
                        bar = "#".ljust(bar_len, "#")

                    text_bar = (
                        f"{title.ljust(15)}:  [{bar}] | partials: {total-count:,.2f}\n"
                    )
                    sys.stdout.write(text_bar)

        except Exception as error:
            logger.error(f"{error}")
