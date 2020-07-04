from dynamodb.dynamodb import DynamoDB
from utils import load_payload, check_payload, success


@load_payload
@check_payload(id='id')
def put_reminder(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).put(Item=kwargs.get('body')))
