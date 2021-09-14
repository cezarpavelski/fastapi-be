from fastapi import FastAPI

from src.payments.infrastructure.containers import Container
from web import routes

container = Container()
container.wire(modules=[routes])

app = FastAPI()
app.container = container
app.include_router(routes.router)
