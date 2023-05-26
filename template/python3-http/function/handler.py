import logging
from .handler_types import Event, Context


def handle(event: Event, context: Context):
    logger: logging.Logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    response: str = 'Hello from OpenFaaS!'
    logger.info(response)
    return {'statusCode': 200, 'body': response}
