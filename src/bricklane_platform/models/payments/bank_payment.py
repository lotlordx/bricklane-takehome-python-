from bricklane_platform.models.payments.abs_payment import Payment
from bricklane_platform.models.bank import Bank


class BankPayment(Payment):
    name = "bank"
    bank_account_id = None

    def __init__(self, data=None):
        if not data:
            return
        super(BankPayment, self).__init__(data)
        bank = Bank()
        bank.bank_account_id = int(data.get("bank_account_id", None))
        self.bank = bank

    def is_successful(self):
        if self.bank.status == "successfully processed" or self.bank.status is None:
            return True
