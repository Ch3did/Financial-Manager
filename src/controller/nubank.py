import arrow
from loguru import logger

from src.controller.debit import Debit_ATM


class FileHandler(Debit_ATM):
    def __init__(self):
        pass

    def import_file(self):
        try:
            pass
        except Exception as error:
            logger.error(error)
