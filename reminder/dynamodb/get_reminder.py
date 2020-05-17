import os
import logging
from dynamodb.get import get

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_reminder(event, context):
    return get(event, context, table=os.environ['DYNAMODB_TABLE'])
