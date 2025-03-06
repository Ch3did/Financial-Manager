import arrow
from loguru import logger
from tabulate import tabulate

from src.controller.category_controller import Category_ATM
from src.helpers.clear import clean_output


class CategoryView:
    @clean_output
    def create_category():
        try:
            print("----------Create New Category")
            print("------------------------------\n")
            name = input("Name: ")
            description = input("Description: ")
            expected = float(input("Expected (%.2): "))
            Category_ATM().add_category(name.lower(), description, expected)
            print(f"Category {name.title()} created sucessfully")
        except Exception as error:
            logger.error(f"{error}")

    @clean_output
    def get_categories(get_invisible):
        print("--------------------------Get  Categories ")
        print("-----------------------------------------\n")
        try:
            data = Category_ATM().get_categories_list(get_invisible)
            if data:

                table = [
                    (
                        "ID",
                        "Name",
                        "Expected",
                        "Description",
                        "Created at",
                    )
                ]
                for item in data:
                    lista = (
                        item.id,
                        item.name,
                        item.expected,
                        item.description,
                        item.created_at,
                    )
                    table.append(lista)

                print(tabulate(table, headers="firstrow"))
            else:
                print(f"Categories Not Found")

        except Exception as error:
            logger.error(f"{error}")
