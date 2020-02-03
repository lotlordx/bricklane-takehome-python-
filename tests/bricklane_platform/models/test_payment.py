import unittest
from datetime import datetime


class TestBankPayment(unittest.TestCase):

    def setUp(self):
        self.payment = BankPayment()

    def test_set_up(self):


        self.assertIsNone(self.payment.customer_id)
        self.assertIsNone(self.payment.date)
        self.assertIsNone(self.payment.amount)
        self.assertIsNone(self.payment.fee)
        self.assertIsNone(self.payment.bank_account_id)

    def test_create_bank_payment(self):

        test_data = {
            "customer_id": "5340",
            "amount": "4433",
            "date": "2001-06-11",
            "bank_account_id": "1000"
        }

        self.payment = BankPayment(test_data)
        self.assertEqual(self.payment.amount, 4433)
        self.assertEqual(self.payment.customer_id, 5340)
        self.assertEqual(self.payment.fee, 2
        self.assertEqual(self.payment.date, datetime(2001, 06, 11))
