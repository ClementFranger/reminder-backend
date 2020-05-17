import os
import logging
from dynamodb.create import create

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_reminder(event, context):
    return create(event, context, table=os.environ['DYNAMODB_TABLE'])
