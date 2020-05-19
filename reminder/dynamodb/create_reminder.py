import json
import os
import logging
from dynamodb.create import create
from utils import validate_params, failure

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_reminder(event, context):
    logger.info('event : {event}'.format(event=event))
    body, = validate_params(body=event.get('body'))

    body = json.loads(body) if isinstance(body, str) else body
    id = body.get('id')
    if not id:
        return failure(code=400, body='You should provide a reminder id to your payload')

    params = {
        'TableName': os.environ['DYNAMODB_TABLE'],
        'Item': body
    }
    return create(key=id, params=params)
