from inspect import getmembers, isclass, isabstract
from bricklane_platform.models import payments


class PaymentFactory(object):
	payment_mode = {}

	def __init__(self):
		self.load_payments()

	def load_payments(self):
		classes = getmembers(payments, lambda m: isclass(m) and not isabstract(m))

		for name, _type in classes:
			if isclass(_type) and issubclass(_type, payments.Payment):
				class_item_dict = {name: _type}
				self.payment_mode.update(class_item_dict)

	def create_instance(self, payment_type):
		payment_type = payment_type.title() + 'Payment'
		if payment_type in self.payment_mode:
			return self.payment_mode[payment_type]
		raise Exception("No payment handler for {}".format(payment_type))