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

    body = json.loads(scan(params=params).get('body'))
    return success(body=json.dumps([d for d in body if
                                    (date.today() - datetime.strptime(d.get('start'), "%d/%m/%Y").date()).days % int(
                                        d.get('frequency')) == 0], cls=DecimalEncoder))
