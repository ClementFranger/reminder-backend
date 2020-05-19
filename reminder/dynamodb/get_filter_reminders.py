import json
import os
import logging
from functools import reduce

from boto3.dynamodb.conditions import Attr

from dynamodb.scan import scan
from utils import validate_params, failure

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_filter_reminders(event, context):
    logger.info('event : {event}'.format(event=event))
    body, = validate_params(body=event.get('body'))

    body = json.loads(body) if isinstance(body, str) else body
    if not (body and body.get('filter')):
        return failure(code=400, body='You should provide a filter to your payload')

    params = {'TableName': os.environ['DYNAMODB_TABLE'],
              'FilterExpression': reduce(lambda a, b: a & b, [Attr(k).eq(v) for k, v in body.get('filter').items()])}
    return scan(event, context, params=params)
