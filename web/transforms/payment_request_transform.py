import re
from datetime import date
from decimal import Decimal
from typing import Union

from src.payments.domain.payment_dto import AddressDto, DocumentDto, CustomerDto, ShippingDto, \
    ItemDto, PaymentDto
from web.validators.payment_request import PaymentRequest


def payment_request_transform(payment_request: PaymentRequest):
    shipping = None
    if payment_request.shipping:
        street = payment_request.shipping.address.address1.split(",")[0]
        address = AddressDto(
            state=payment_request.shipping.address.state,
            city=payment_request.shipping.address.city,
            street=street,
            street_number=payment_request.shipping.address.number,
            zipcode=payment_request.shipping.address.zipcode,
            country=payment_request.shipping.address.country
        )
        shipping = ShippingDto(
            name=payment_request.shipping.name,
            fee=_convert_currency_to_cents(payment_request.shipping.fee),
            expedited=True,
            address=address,
            delivery_date=str(date.today()),
        )

    document = DocumentDto(
        type="cpf",
        number=_clean_document_chars(payment_request.customer.document)
    )

    customer = CustomerDto(
        external_id=payment_request.customer.id,
        name=payment_request.customer.name,
        type="individual",
        email=payment_request.customer.email,
        documents=[document],
        phone_numbers=[_clean_phone_number(payment_request.customer.phone_number)],
        country="br",
    )

    items = []
    for item in payment_request.products:
        items.append(
            ItemDto(
                id=str(item.id),
                title=item.title,
                unit_price=_convert_currency_to_cents(item.unit_price),
                quantity=item.quantity,
                tangible=True,
            )
        )

    transaction = PaymentDto(
        card_number=payment_request.card_number,
        card_expiration_date=payment_request.card_expiration_date,
        card_holder_name=payment_request.card_holder_name,
        amount=_convert_currency_to_cents(payment_request.amount),
        card_cvv=payment_request.card_cvv,
        customer=customer,
        shipping=shipping,
        items=items,
    )

    return transaction


def _clean_document_chars(number):
    return re.sub(r"\D", "", number)


def _clean_phone_number(number):
    number_without_symbols = re.sub(r"\D", "", number.replace("+550", "+55"))
    return f"+{number_without_symbols}"


def _convert_currency_to_cents(value: Union[float, Decimal]):
    value_to_parse = Decimal(str(value))
    return int(value_to_parse * 100)
