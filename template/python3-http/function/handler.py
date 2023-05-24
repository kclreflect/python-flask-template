import logging


def handle(event, context):
    logger: logging.Logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    response: str = 'Hello from OpenFaaS!'
    logger.info(response)
    return {'statusCode': 200, 'body': response}
