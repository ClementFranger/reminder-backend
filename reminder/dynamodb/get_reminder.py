import os
import logging
from dynamodb.get import get
from utils import validate_params, failure

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_reminder(event, context):
    logger.info('event : {event}'.format(event=event))
    path, = validate_params(path=event.get('pathParameters'))

    id = path.get('id')
    if not id:
        return failure(code=400, body='You should provide a id to your path parameters')

    params = {
        'TableName': os.environ['DYNAMODB_TABLE'],
        'Key': {'id': id}
    }
    return get(event, context, key=id, params=params)
