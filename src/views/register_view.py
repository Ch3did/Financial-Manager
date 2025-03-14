from loguru import logger

from src.controller.register_controller import RegisterController
from src.helpers.clear import clean_output
from src.helpers.exception import InputException
from src.views.output import Output


class RegisterView(Output):
    def __init__(self):
        super().__init__()
        self.register = RegisterController()

    @clean_output
    def new_register(self):
        try:
            self._make_rodape("Create New Register")
            register_dict = self._ask_about_register()
            self.register.create_register(register_dict)

        except InputException as error:
            logger.error(f"{error}")
