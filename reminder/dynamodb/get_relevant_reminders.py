import os
import logging
from dynamodb.scan import scan
from boto3.dynamodb.conditions import Attr

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_relevant_reminders(event, context):
    return scan(event, context, table=os.environ['DYNAMODB_TABLE'], filter=Attr('id').eq('test'))
