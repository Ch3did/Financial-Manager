from src.helpers.connection import Database
from src.helpers.exception import ATMException
from src.models.category import Category


class Category_ATM:
    def __init__(self):

        self.conn = Database().session()

    def add_category(self, name, description, expected):
        if self.conn.query(Category.id).filter(Category.name == name.rstrip()).first():
            raise ATMException(
                message="Category already exists... ",
                description=description,
                expected=expected,
            )
        category = Category(
            name=name, description=description, expected=expected, is_visible=True
        )

        if float(expected) < 0:
            Category.is_spend = True

        self.conn.add(category)
        self.conn.commit()
        self.conn.close()

    def get_category_list(self, get_invisible):
        if get_invisible == False:  # VISIBLE
            return self.conn.query(Category).filter(Category.is_visible == True).all()
        if get_invisible == True:  # ALL
            return self.conn.query(Category).all()

    def get_category_by_id(self, id):
        return [self.conn.query(Category).filter(Category.id == id).first()]
