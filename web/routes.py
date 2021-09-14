from dependency_injector.wiring import Provide, inject
from fastapi import Depends, APIRouter
from starlette.responses import JSONResponse

from src.payments.application.create_payment_credit import CreatePaymentCredit
from src.payments.application.create_payment_credit1 import CreatePaymentCredit1
from src.payments.infrastructure.Getnet.getnet_acquirer_gateway_credit import GetnetAcquirerGatewayCredit
from src.payments.infrastructure.Pagarme.pagarme_acquirer_gateway_credit import PagarmeAcquirerGatewayCredit
from src.payments.infrastructure.containers import Container
from web.resources.payment_response_resource import PaymentResponseResource
from web.validators.payment_request import PaymentRequest
from web.transforms.payment_request_transform import payment_request_transform

router = APIRouter()


@router.get("/")
async def health_check():
    return {"Hello": "World"}


@router.post("/payments", status_code=201, response_model=PaymentResponseResource)
@inject
async def payments(payment_request: PaymentRequest,
                   create_payment: CreatePaymentCredit = Depends(Provide[Container.create_payment])):
    try:
        payment = payment_request_transform(payment_request)

        return PaymentResponseResource.from_payment(create_payment.create(payment))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Payment1 error: {e.args}"})


@router.post("/payments1", status_code=201, response_model=PaymentResponseResource)
async def payments(payment_request: PaymentRequest):
    try:
        payment = payment_request_transform(payment_request)
        create_payment = CreatePaymentCredit1([
            PagarmeAcquirerGatewayCredit(),
            GetnetAcquirerGatewayCredit(),
        ])

        return PaymentResponseResource.from_payment(create_payment.create(payment))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Payment1 error: {e.args}"})
