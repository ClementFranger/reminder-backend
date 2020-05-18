import os
import logging
from dynamodb.scan import scan

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_all_reminder(event, context):
    return scan(event, context, table=os.environ['DYNAMODB_TABLE'])
