from functools import reduce
from boto3.dynamodb.conditions import Attr

from dynamodb.dynamodb import DynamoDB
from utils import success, load_payload


@load_payload
def filter_scan_reminders(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).scan(
        FilterExpression=reduce(lambda a, b: a & b, [Attr(k).eq(v) for k, v in kwargs.get('body').items()])).get(
        'Items'))
