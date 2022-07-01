from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Transaction:
    qualifier: str
    post_date: date
    transaction_date: date
    description: str
    amount: Decimal
