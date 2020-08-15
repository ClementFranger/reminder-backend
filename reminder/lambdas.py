import json
from datetime import date, datetime
from functools import wraps

from lambdas.lambdas import Lambdas
from reminder.dynamodb import Reminder
from utils import DecimalEncoder


class LambdasReminder(Lambdas):
    _REMINDER = Reminder()

    class Decorators(object):
        @classmethod
        def output(cls, f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                result = f(*args, **kwargs)
                return {'statusCode': 200, 'headers': kwargs.get('headers'),
                        'body': json.dumps(result, cls=DecimalEncoder)}
            return wrapper

    def _today(self, reminders):
        result = []
        for r in reminders:
            days = (date.today() - datetime.strptime(r.get(self._REMINDER.Schema.START), "%d/%m/%Y").date()).days
            frequency = int(r.get(self._REMINDER.Schema.FREQUENCY))
            if (frequency == 0 and days == 0) or (frequency != 0 and days % frequency == 0):
                result.append(r)
        return result

    @Lambdas.Decorators.output
    def scan(self, *args, **kwargs):
        return self._REMINDER.scan()

    @Lambdas.Decorators.output
    @Lambdas.Decorators.payload(id=Reminder.Schema.ID)
    def get(self, *args, **kwargs):
        return self._REMINDER.get(Key=kwargs.get('path'))

    @Lambdas.Decorators.cors(ips=[r"^https://master\..+\.amplifyapp\.com$", r"^http://localhost:3000$"])
    @Lambdas.Decorators.output
    @Lambdas.Decorators.payload(id=Reminder.Schema.ID)
    def put(self, *args, **kwargs):
        return self._REMINDER.put(Item=kwargs.get('body'))

    @Lambdas.Decorators.cors(ips=[r"^https://master\..+\.amplifyapp\.com$", r"^http://localhost:3000$"])
    @Decorators.output
    def today(self, *args, **kwargs):
        reminders = self._REMINDER.scan(**kwargs).get('Items')
        return self._today(reminders)


put = LambdasReminder().put
today = LambdasReminder().today
