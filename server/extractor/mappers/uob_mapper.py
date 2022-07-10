import re
from datetime import datetime
from decimal import Decimal

from extractor.dto import Transaction


class UOBAccountMapper:
    @staticmethod
    def map_transactions(data):
        pass


class UOBCardMapper:
    @staticmethod
    def map_transactions(data: dict) -> list[Transaction]:
        transactions: list[Transaction] = []
        i = 0
        card = data['card_details'][i]
        num_cards = len(data['card_details'])
        statement_date = datetime.strptime(data['statement_date'], '%Y-%m-%d')
        running_sum = Decimal(0)

        for transaction in data['transactions']:
            if match := re.match(r'TOTAL BALANCE FOR (.+)$', transaction['description']):
                assert match.group(1) == card['name']
                assert transaction['amount'] == card['amount_due']
                assert Decimal(transaction['amount']) == running_sum
                i += 1
                running_sum = Decimal(0)
                if i < num_cards:
                    card = data['card_details'][i]
            else:
                date_pattern = r'\d{2} ({\w{3}})'
                # Post date parsing
                if transaction['post_date']:
                    post_match = re.match(date_pattern, transaction['post_date'])
                    if statement_date.month == 1 and post_match.group(1) == 'DEC':
                        post_year = statement_date.year - 1
                    else:
                        post_year = statement_date.year
                    post_date = datetime.strptime(transaction['post_date'] + ' ' + str(post_year), '%d %b %Y')
                else:
                    post_date = None
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
                # Reference parsing
                if transaction['reference']:
                    reference = re.match(r'Ref No\. : (\d+)', transaction['reference']).group(1)
                else:
                    reference = None

                transactions.append(Transaction(
                    data['organization'],
                    data['statement_type'],
                    card['number'],
                    post_date,
                    trans_date,
                    transaction['description'],
                    reference,
                    amount
                ))

        return transactions
