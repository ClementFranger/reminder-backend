from datetime import date, datetime

from dynamodb.dynamodb import DynamoDB
from utils import success, cors


@cors(ips=['*'])
def get_today_reminders(event, context, **kwargs):
    return success(body=today_reminders(DynamoDB(**kwargs).scan().get('Items')), headers={'Access-Control-Allow-Origin': '*'})


def today_reminders(reminders):
    result = []
    for r in reminders:
        days = (date.today() - datetime.strptime(r.get('start'), "%d/%m/%Y").date()).days
        frequency = int(r.get('frequency'))
        if (frequency == 0 and days == 0) or (frequency != 0 and days % frequency == 0):
            result.append(r)
    return result
