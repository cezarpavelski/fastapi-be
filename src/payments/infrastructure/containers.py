from dependency_injector import containers, providers

from src.payments.application.create_payment_credit import CreatePaymentCredit
from src.payments.infrastructure.Getnet.getnet_acquirer_gateway_credit import GetnetAcquirerGatewayCredit
from src.payments.infrastructure.Pagarme.pagarme_acquirer_gateway_credit import PagarmeAcquirerGatewayCredit


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    pagarme_acquirer = providers.Resource(
        PagarmeAcquirerGatewayCredit,
    )

    getnet_acquirer = providers.Resource(
        GetnetAcquirerGatewayCredit,
    )

    create_payment = providers.Factory(
        CreatePaymentCredit,
        pagarme=pagarme_acquirer,
        getnet=getnet_acquirer,
    )
