import hashlib
from typing import List, Optional

from pydantic import BaseModel


class CustomerRequest(BaseModel):
    customer_ip: str
    name: str
    email: str
    phone_number: str
    document: str
    age: int

    @property
    def id(self):
        return hashlib.md5(f"{self.email}{self.phone_number}".encode()).hexdigest()


class AddressRequest(BaseModel):
    address1: str
    zipcode: str
    state: str
    city: str
    country: str
    number: str
    address2: str


class ShippingRequest(BaseModel):
    name: str
    fee: int
    address: AddressRequest


class SellerRequest(BaseModel):
    id: int
    name: str
    created_at: str


class ProductItemRequest(BaseModel):
    id: int
    title: str
    quantity: int
    unit_price: float
    category: str


class PaymentRequest(BaseModel):
    card_id: Optional[str] = None
    card_number: Optional[str] = None
    card_expiration_date: Optional[str] = None
    card_holder_name: Optional[str] = None
    card_cvv: str
    amount: float
    capture: bool
    checkout_id: str
    encrypted_card_number: str
    customer:  CustomerRequest
    shipping:  Optional[ShippingRequest]
    seller:  Optional[SellerRequest]
    products: List[ProductItemRequest]
