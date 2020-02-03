from decimal import Decimal
from dateutil.parser import parse
from abc import ABCMeta, abstractmethod

from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):
    __metaclass__ = ABCMeta

    customer_id = None
    date = None
    amount = None
    fee = None

    @abstractmethod
    def __init__(self, data):
        self.customer_id = int(data.get("customer_id", None))
        self.date = parse(data.get("date", None))

        total_amount = Decimal(data.get("amount", None))
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

    @abstractmethod
    def is_successful(self):
        pass

