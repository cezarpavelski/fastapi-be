from src.payments.domain.acquirer_contract import AcquirerContract
from src.payments.domain.payment_dto import PaymentDto
from src.payments.domain.payment_response import PaymentResponse


class PagarmeAcquirerGatewayCredit(AcquirerContract):
    def payment(self, payment: PaymentDto) -> PaymentResponse:
        # raise Exception('Pagarme error')
        return PaymentResponse(
            id="xxxxxxx",
            checkout_id="ddddddd",
            cost_to_seller=10,
            amount=payment.amount,
            status="dddddd",
            card_last_digits="3333",
            card_brand="master",
            created_at="2020-01-01",
            acquirer="pagarme",
        )

    def capture(self):
        pass

    def refund(self):
        pass

    def tokenize(self):
        pass

    def webhook(self):
        pass
