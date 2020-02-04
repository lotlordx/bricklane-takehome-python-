import unittest

from datetime import datetime
from decimal import Decimal
from bricklane_platform.models.payments import BankPayment, CardPayment
from bricklane_platform.models.bank import Bank
from bricklane_platform.models.card import Card


class TestBankPayment(unittest.TestCase):

    def setUp(self):
        self.payment_mode = BankPayment()
        self.bank = Bank()

    def test_bank_payment_set_up(self):

        self.assertIsNone(self.payment_mode.customer_id)
        self.assertIsNone(self.payment_mode.date)
        self.assertIsNone(self.payment_mode.amount)
        self.assertIsNone(self.payment_mode.fee)
        self.assertIsNone(self.payment_mode.bank_account_id)

    def test_make_bank_payment(self):

        bank_payment_details = {
            "customer_id": "5340",
            "amount": "4433",
            "date": "2001-06-11",
            "bank_account_id": "1000"
        }

        self.payment_mode = BankPayment(bank_payment_details)
        self.assertEqual(self.payment_mode.amount, Decimal("4344.34"))
        self.assertEqual(self.payment_mode.customer_id, 5340)
        self.assertEqual(self.payment_mode.fee, Decimal("88.66"))
        self.assertEqual(self.payment_mode.date, datetime(2001, 06, 11))

    def test_bank_payment_processed(self):
        self.bank.status = "successfully processed"
        self.payment_mode.bank = self.bank
        self.assertTrue(self.payment_mode.is_successful())

    def test_bank_payment_falied(self):
        self.bank.status = "transaction failed"
        self.payment_mode.bank = self.bank
        self.assertFalse(self.payment_mode.is_successful())

    def test_bank_payment_had_error(self):
        self.bank.status = "an error occured"
        self.payment_mode.bank = self.bank
        self.assertFalse(self.payment_mode.is_successful())


class TestCardPayment(unittest.TestCase):

    def setUp(self):
        self.payment_mode = CardPayment()
        self.card = Card()

    def test_card_payment_set_up(self):
        self.assertIsNone(self.payment_mode.customer_id)
        self.assertIsNone(self.payment_mode.date)
        self.assertIsNone(self.payment_mode.amount)
        self.assertIsNone(self.payment_mode.fee)

    def test_make_card_payment(self):
        card_payment_details = {
            "customer_id": "4389498438943",
            "amount": "4433",
            "date": "2001-06-11",
            "card_id": "98743438943843",
            "card_status": "processed"
        }

        self.payment_mode = CardPayment(card_payment_details)
        self.assertEqual(self.payment_mode.amount, Decimal("4344.34"))
        self.assertEqual(self.payment_mode.customer_id, 4389498438943)
        self.assertEqual(self.payment_mode.card.status, "processed")
        self.assertEqual(self.payment_mode.fee, Decimal("88.66"))
        self.assertEqual(self.payment_mode.date, datetime(2001, 06, 11))

    def test_card_payment_processed(self):
        self.card.status = "processed"
        self.payment_mode.card = self.card
        self.assertTrue(self.payment_mode.is_successful())

    def test_card_payment_falied(self):
        self.card.status = "declined"
        self.payment_mode.card = self.card
        self.assertFalse(self.payment_mode.is_successful())

    def test_card_payment_had_error(self):
        self.card.status = "an error occured"
        self.payment_mode.card = self.card
        self.assertFalse(self.payment_mode.is_successful())


