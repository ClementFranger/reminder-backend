import json
import os
import logging
from datetime import date, datetime

from dynamodb.scan import scan
from utils import success, DecimalEncoder

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_today_reminders(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {'TableName': os.environ['DYNAMODB_TABLE']}

    body = today_reminders(json.loads(scan(params=params).get('body')))

    return success(body=json.dumps(body), cls=DecimalEncoder)


def today_reminders(reminders):
    result = []
    for r in reminders:
        days = (date.today() - datetime.strptime(r.get('start'), "%d/%m/%Y").date()).days
        frequency = int(r.get('frequency'))
        if (frequency == 0 and days == 0) or (frequency != 0 and days % frequency == 0):
            result.append(r)
    return result
