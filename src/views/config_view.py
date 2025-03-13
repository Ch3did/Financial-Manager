import sys

from loguru import logger

from src.helpers.clear import clean_output
from src.helpers.exception import DatabaseException, ExtractionException
from src.views.output import Output
from src.controller.config_controller import ConfigController


class ConfigView(Output):
    def __init__(self):
        super().__init__()
        self.config = ConfigController()
        
        
    @clean_output
    def run_migrate(self):
        try:
            self.make_migrate()
            logger.info("Tables Ready")

        except DatabaseException as error:
            logger.error(f"Tables are Down... {error}")

    @clean_output
    def make_homescreen(self):
        try:
            categories = self.config._get_category_list()
            self._make_rodape("Home Screen")
            transactions = self.config.get_transactions()
            bar_len = 45
            
            # Logica para organizar as Transacoes por Category
            category_plot_dict = {}
            for transaction in transactions:
                if transaction.category_id:
                    if transaction.category_id not in category_plot_dict:
                        category_id = categories[transaction.category_id +1]
                        category_plot_dict[category_id].name = 0
                    category_plot_dict[category_id].name += category_plot_dict[category_id].value

            # Logica para plor em barra 
            for category in categories:
                count = abs(category_plot_dict.get(category.name, 0))
                total = abs(category.expected)
                title = category.name.title()

                if total > count:
                    filled_len = int(round(bar_len * float(count) / float(total)))
                    bar = "#" * filled_len + "-" * (bar_len - filled_len)
                else:
                    bar = "#".ljust(bar_len, "#")

                text_bar = f"{title.ljust(15)}:  [{bar}] | partials: {total-count:,.2f}\n"
                sys.stdout.write(text_bar)
            
        except ExtractionException  as error:
            logger.error(f"{error}")
