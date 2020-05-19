import os
import logging
from datetime import date

from boto3.dynamodb.conditions import Attr

from dynamodb.get_all_reminders import get_all_reminders
from dynamodb.scan import scan

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_today_reminders(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {'TableName': os.environ['DYNAMODB_TABLE']}
    days = (date.today() - date(2020, 1, 1)).days
    return [d for d in scan(event, context, params=params) if days % d.frequency == 0]
