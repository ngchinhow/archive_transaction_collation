import re
from datetime import datetime
from decimal import Decimal

from extractor.dto import Transaction


class OCBCAccountMapper:
    @staticmethod
    def map_transactions(data: dict) -> list[Transaction]:
        transactions: list[Transaction] = []
        start_amount = None
        running_sum = Decimal(0)
        statement_date = datetime.strptime(data['statement_date'], '%Y-%m-%d')

        for transaction in data['transactions']:
            # Description parsing
            description = transaction['description'].replace(r'\/', '/')
            if description == 'BALANCE B/F':
                start_amount = Decimal(transaction['balance'])
                continue
            if description == 'BALANCE C/F':
                assert Decimal(transaction['balance']) == start_amount + running_sum
                continue

            date_pattern = r'\d{2} ({\w{3}})'
            # Value date parsing
            if transaction['value_date']:
                value_match = re.match(date_pattern, transaction['value_date'])
                if statement_date.month == 1 and value_match.group(1) == 'DEC':
                    value_year = statement_date.year - 1
                else:
                    value_year = statement_date.year
                value_date = datetime.strptime(transaction['value_date'] + ' ' + str(value_year), '%d %b %Y')
            else:
                value_date = None
            # Trans date parsing
            if transaction['trans_date']:
                trans_match = re.match(date_pattern, transaction['trans_date'])
                if statement_date.month == 1 and trans_match.group(1) == 'DEC':
                    trans_year = statement_date.year - 1
                else:
                    trans_year = statement_date.year
                trans_date = datetime.strptime(transaction['trans_date'] + ' ' + str(trans_year), '%d %b %Y')
            else:
                trans_date = None
            # Amount parsing
            amount = Decimal(transaction['amount'])
            running_sum += amount

            transactions.append(Transaction(
                data['organization'],
                data['statement_type'],
                data['account_number'],
                value_date,
                trans_date,
                description,
                "",
                amount
            ))

        return transactions


class OCBCCardMapper:
    @staticmethod
    def map_transactions(data):
        pass
