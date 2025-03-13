from loguru import logger

from src.controller.category_controller import CategoryController
from src.helpers.clear import clean_output
from src.helpers.exception import ExtractionException, InputException
from src.views.output import Output


class CategoryView(Output):
    def __init__(self):
        super().__init__()
        self.category = CategoryController()

    @clean_output
    def new_category(self):
        try:
            self._make_rodape("Create New Category")
            category_dict = self._ask_about_category()
            self.category.create_category(category_dict)

        except InputException as error:
            logger.error(f"{error}")

    @clean_output
    def get_categories(self):
        try:
            self._make_rodape("Get  Categories")
            data = self.category.get_category()
            self.return_tabulated_data(data)
        except ExtractionException as error:
            logger.error(f"{error}")
