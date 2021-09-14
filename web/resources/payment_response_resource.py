from pydantic import BaseModel

from src.payments.domain.payment_response import PaymentResponse


class PaymentResponseResource(BaseModel):
    acquirer: str
    amount: float
    card_brand: str
    card_last_digits: str
    checkout_id: str
    cost_to_seller: int
    created_at: str
    id: str
    status: str

    @staticmethod
    def from_payment(payment: PaymentResponse):
        return PaymentResponseResource(
            id=str(payment.id),
            checkout_id=payment.checkout_id,
            cost_to_seller=payment.cost_to_seller,
            amount=payment.amount,
            status=payment.status,
            card_last_digits=payment.card_last_digits,
            card_brand=payment.card_brand,
            created_at=payment.created_at,
            acquirer=payment.acquirer,
        )
