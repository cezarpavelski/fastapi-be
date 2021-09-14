import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentResponse:
    checkout_id: str
    cost_to_seller: int
    amount: float
    status: str
    card_last_digits: str
    card_brand: str
    id: uuid
    created_at: str
    acquirer: str
