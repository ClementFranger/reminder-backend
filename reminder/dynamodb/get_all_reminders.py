import os
import logging
from dynamodb.scan import scan

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_all_reminders(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {'TableName': os.environ['DYNAMODB_TABLE']}
    return scan(params=params)
