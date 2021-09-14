from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class AddressDto:
    state: str
    city: str
    street: str
    street_number: str
    zipcode: str
    country: str = "br"


@dataclass(frozen=True)
class DocumentDto:
    type: str
    number: str


@dataclass(frozen=True)
class CustomerDto:
    external_id: str
    name: str
    type: str
    email: str
    documents: List[DocumentDto]
    phone_numbers: List[str]
    country: str = "br"


@dataclass(frozen=True)
class ShippingDto:
    name: str
    fee: int
    address: AddressDto
    expedited: bool = True
    delivery_date: str = None


@dataclass(frozen=True)
class ItemDto:
    id: str
    title: str
    unit_price: int
    quantity: int
    tangible: bool = True


@dataclass(frozen=True)
class PaymentDto:
    amount: int
    card_cvv: str
    customer: CustomerDto
    shipping: ShippingDto
    items: List[ItemDto]

    card_id: Optional[str] = None
    card_number: Optional[str] = None
    card_expiration_date: Optional[str] = None
    card_holder_name: Optional[str] = None

    reference_key: str = None
    payment_method: str = "credit_card"
    capture: bool = False
    soft_descriptor: str = "Pagamento Ze Delivery"
    transaction_async: bool = False
