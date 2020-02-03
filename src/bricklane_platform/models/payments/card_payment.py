from bricklane_platform.models.card import Card
from bricklane_platform.models.payments.abs_payment import Payment


class CardPayment(Payment):
    card_id = None
    name = "card"

    def __init__(self, data=None):
        if not data:
            return
        super(CardPayment, self).__init__(data)
        card = Card()
        card.card_id = int(data.get("card_id", None))
        card.status = data.get("card_status", None)
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"