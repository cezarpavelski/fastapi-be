from src.payments.domain.acquirer_contract import AcquirerContract
from src.payments.domain.payment_dto import PaymentDto


class CreatePaymentCredit:
    _i = 0

    def __init__(self, pagarme: AcquirerContract, getnet: AcquirerContract):
        self._acquirers = (pagarme, getnet)

    def create(self, payment: PaymentDto):
        try:
            return self._acquirers[self._i].payment(payment)
        except Exception as e:
            if self._i < len(self._acquirers) - 1:
                self._i += 1
                return self.create(payment)
            raise e
