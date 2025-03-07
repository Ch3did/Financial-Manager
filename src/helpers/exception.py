class BasicException(Exception):
    def __init__(self, message):
        self.message = message
class FinancialExeption(BasicException):
    ...
    
class ExtractionException(BasicException):
    ...
    
class DatabaseException(BasicException):
    ...