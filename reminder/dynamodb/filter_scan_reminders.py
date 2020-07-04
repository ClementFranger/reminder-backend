import json
from functools import reduce

from boto3.dynamodb.conditions import Attr


from dynamodb.dynamodb import DynamoDB
from utils import failure, success, load_payload


@load_payload
def filter_scan_reminders(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).scan(FilterExpression=reduce(lambda a, b: a & b, [Attr(k).eq(v) for k, v in kwargs.get('body').items()])).get('Items'))
    # logger.info('event : {event}'.format(event=event))
    # body, = validate_params(body=event.get('body'))
    #
    # body = json.loads(body) if isinstance(body, str) else body
    # if not (body and body.get('filter')):
    #     return failure(code=400, body='You should provide a filter to your payload')
    #
    # params = {'TableName': os.environ['DYNAMODB_TABLE'],
    #           'FilterExpression': reduce(lambda a, b: a & b, [Attr(k).eq(v) for k, v in body.get('filter').items()])}
    # return scan(params=params)
