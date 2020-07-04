import json
import os
import unittest

from dynamodb.filter_scan_reminders import filter_scan_reminders
# from dynamodb.get_reminder import get_reminder
from dynamodb.put_reminder import put_reminder
from dynamodb.scan_reminders import scan_reminders


class TestDynamoDB(unittest.TestCase):
    __DYNAMODB_TABLE__ = 'reminder'
    __event__ = {'body': None, 'pathParameters': None, 'queryStringParameters': None}
    __context__ = None
    __mock__ = os.path.dirname(os.getcwd()) + '\mock\dynamodb\{mock}.json'

    def test_put_reminder(self):
        with open(self.__mock__.format(mock='put_reminder'), "r") as mock:
            self.__event__['body'] = json.dumps(json.loads(mock.read()).get('body'))
        result = put_reminder(self.__event__, self.__context__, DYNAMODB_TABLE=self.__DYNAMODB_TABLE__)
        self.assertIsInstance(result, dict)

    # def test_get_reminder(self):
    #     with open(self.__mock__.format(mock='get_reminder'), "r") as mock:
    #         self.__event__['body'] = json.dumps(json.loads(mock.read()).get('body'))
    #     result = get_reminder(self.__event__, self.__context__, DYNAMODB_TABLE=self.__DYNAMODB_TABLE__)
    #     self.assertIsInstance(result, dict)

    def test_scan_reminders(self):
        result = scan_reminders(self.__event__, self.__context__, DYNAMODB_TABLE=self.__DYNAMODB_TABLE__)
        self.assertIsInstance(result, dict)

    def test_filter_scan_reminders(self):
        with open(self.__mock__.format(mock='filter_scan_reminders'), "r") as mock:
            self.__event__['body'] = json.dumps(json.loads(mock.read()).get('body'))
        result = filter_scan_reminders(self.__event__, self.__context__, DYNAMODB_TABLE=self.__DYNAMODB_TABLE__)
        self.assertIsInstance(result, dict)
