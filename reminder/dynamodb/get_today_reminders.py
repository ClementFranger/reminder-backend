import json
import os
import logging
from datetime import date

from dynamodb.scan import scan
from utils import success, DecimalEncoder

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_today_reminders(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {'TableName': os.environ['DYNAMODB_TABLE']}

    days = (date.today() - date(date.today().year, 1, 1)).days
    return success(body=json.dumps([d for d in json.load(scan(params=params).get('body')) if days % d.frequency == 0],
                                   cls=DecimalEncoder))
