import xml.etree.ElementTree as ET
from typing import List

from loguru import logger

from src.controller.database_controller import Database
from src.helpers import parse_date, read_ofx_file
from src.models.register import OFXRegister
from src.models.transaction import Transaction


class TransactionController(Database):
    def import_file(self, path: str):
        try:
            data = ET.fromstring(read_ofx_file(path))
            self.create_transaction(data)
            self.create_register(data)
            logger.info("Import Sucessfully")
        except Exception as err:
            print(err)

    def create_transaction(self, ofx_data: dict) -> Transaction:
        for stmttrn in ofx_data.findall(".//STMTTRN"):
            transaction = Transaction(
                description=stmttrn.find("MEMO").text,
                date=parse_date(stmttrn.find("DTPOSTED").text),
                value=float(stmttrn.find("TRNAMT").text),
                transaction_type=stmttrn.find("TRNTYPE").text,
                transaction_id=stmttrn.find("FITID").text,
                organization=ofx_data.find(".//FI/ORG").text,
                org_id=ofx_data.find(".//FI/FID").text,
                account=ofx_data.find(".//ACCTID").text,
            )

            self._add_debit(transaction)

    def create_register(self, ofx_data) -> OFXRegister:
        register = OFXRegister(
            org_id=ofx_data.find(".//FI/FID").text,
            account=ofx_data.find(".//ACCTID").text,
            start_date=parse_date(ofx_data.find(".//BANKTRANLIST/DTSTART").text),
            end_date=parse_date(ofx_data.find(".//BANKTRANLIST/DTEND").text),
            organization=ofx_data.find(".//FI/ORG").text,
            amount=float(ofx_data.find(".//LEDGERBAL/BALAMT").text),
        )
        self._add_register(register)

    def get_incomplete_transactions(self) -> List[Transaction]:
        return self._get_transactions_without_category()

    def update_transaction_category(self, transaction: Transaction) -> None:
        self._update_transaction(transaction)

    def get_transactions(self, limit: int = 10):
        return self._get_transactions_with_limit(limit)
