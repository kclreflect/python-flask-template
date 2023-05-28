import logging
from handler_types import Event, Context


def handle(event: Event, context: Context) -> Context:
    logger: logging.Logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    response: str = 'Hello from OpenFaaS!'
    logger.info(response)
    context.statusCode = 200
    context.body = response
    return context
