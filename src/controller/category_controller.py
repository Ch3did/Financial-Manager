from typing import List

from src.controller.database_controller import Database
from src.models.category import Category


class CategoryController(Database):

    def create_category(self, data: dict) -> Category:
        category = Category(
            name=data["name"],
            description=data["description"],
            expected=data["expected"],
        )

        if float(category.expected) < 0:
            Category.is_spend = True

    def get_category(self) -> List[Category]:
        return self._get_category_list()
