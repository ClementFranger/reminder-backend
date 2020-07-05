from dynamodb.dynamodb import DynamoDB
from utils import load_payload, check_payload, success, cors


@cors(ips=[r"^https://master\..+\.amplifyapp\.com$", r"^http://localhost:3000$"])
@load_payload
@check_payload(id='id')
def put_reminder(event, context, **kwargs):
    return success(body=DynamoDB(**kwargs).put(Item=kwargs.get('body')))
