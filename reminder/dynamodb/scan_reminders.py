from dynamodb.dynamodb import DynamoDB
from utils import success


def scan_reminders(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).scan().get('Items'))
