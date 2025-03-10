from datetime import datetime
from typing import List

from sqlmodel import SQLModel
from tabulate import tabulate


class Output:
    def __init__(self):
        self.total_lenght = 30
        self.restricted_columns = ["id", "transaction_id", "category_id"]

    def _get_columns(self, model_class: type[SQLModel]) -> list[str]:
        return [
            field
            for field in model_class.__annotations__.keys()
            if hasattr(model_class, "__fields__") and field in model_class.__fields__
        ]

    def _get_visible_columns(self, model_class: type[SQLModel]) -> list[str]:
        all_columns = self._get_columns(model_class)

        return [
            column for column in all_columns if column not in self.restricted_columns
        ]

    def _make_rodape(self, name: str):
        length = len(name)
        padding = self.total_lenght - length
        print("-" * padding + name)
        print("-" * self.total_lenght)

    def _make_transaction_update_form(self):
        pass

    def _ask_about_category(self) -> dict:
        return {
            "name": input("Name: "),
            "description": input("Description: "),
            "expected": float(input("Expected (%.2): ")),
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }

    def return_tabulated_data(self, data: List[SQLModel]) -> None:
        debit_list = []
        if data:
            headers = self._get_visible_columns(data[0])
            debit_list.append(headers)
            for item in data:
                item.description = item.description[:15]
                row = [getattr(item, column, None) for column in headers]
                debit_list.append(row)
            print(tabulate(debit_list, headers="firstrow", tablefmt="grid"))
        else:
            raise ValueError("No Record was found...")
