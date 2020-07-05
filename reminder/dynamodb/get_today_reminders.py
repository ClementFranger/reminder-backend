from datetime import date, datetime

from dynamodb.dynamodb import DynamoDB
from utils import success, cors


@cors(ips=['https://master.d2as5trm2mnw5s.amplifyapp.com'])
def get_today_reminders(event, context, **kwargs):
    print(kwargs)
    return success(body=today_reminders(DynamoDB(**kwargs).scan().get('Items')), **kwargs)


def today_reminders(reminders):
    result = []
    for r in reminders:
        days = (date.today() - datetime.strptime(r.get('start'), "%d/%m/%Y").date()).days
        frequency = int(r.get('frequency'))
        if (frequency == 0 and days == 0) or (frequency != 0 and days % frequency == 0):
            result.append(r)
    return result
