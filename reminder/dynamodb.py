import logging
import os

from dynamodb.dynamodb import DynamoDB
from utils import Schema

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Reminder(DynamoDB):
    _TABLE_NAME = os.environ.get('REMINDER_TABLE')

    class Schema(Schema):
        ID = 'id'
        DESCRIPTION = 'description'
        FREQUENCY = 'frequency'
        START = 'start'
