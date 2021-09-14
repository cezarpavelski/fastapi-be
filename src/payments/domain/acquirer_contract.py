from typing import Protocol

from src.payments.domain.payment_dto import PaymentDto
from src.payments.domain.payment_response import PaymentResponse


class AcquirerContract(Protocol):
    def payment(self, payment: PaymentDto) -> PaymentResponse:
        pass

    def capture(self):
        pass

    def refund(self):
        pass

    def tokenize(self):
        pass

    def webhook(self):
        pass
