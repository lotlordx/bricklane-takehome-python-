import csv

from bricklane_platform.factory.payment_factory import PaymentFactory


class PaymentProcessor(object):

    def __init__(self, payment_handler= None):
        self.payment_handler = payment_handler or PaymentFactory()

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                payment_handler_class = self.payment_handler.create_instance(source)
                payments.append(payment_handler_class(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
