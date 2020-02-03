import csv

from bricklane_platform.models.payment import Payment

from bricklane_platform.factory.payment_factory import PaymentFactory


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        payment_handler = PaymentFactory()
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                payment_handler_class = payment_handler.create_instance(source)
                payments.append(payment_handler_class(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
