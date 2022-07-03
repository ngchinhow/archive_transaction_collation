from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transaction:
    organization: str
    statement_type: str
    qualifier: str
    post_date: date
    transaction_date: date
    description: str
    reference: str
    amount: Decimal
