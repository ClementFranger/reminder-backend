from dynamodb.dynamodb import DynamoDB
from utils import success, load_payload, check_payload


@load_payload
@check_payload(id='id')
def get_reminder(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).get(Key=kwargs.get('path')).get('Item'))
