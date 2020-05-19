import os
import logging

from boto3.dynamodb.conditions import Attr

from dynamodb.scan import scan

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_today_reminders(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {'TableName': os.environ['DYNAMODB_TABLE'],
              'FilterExpression': Attr('id').eq('test')}
    return scan(event, context, params=params)
