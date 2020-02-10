import unittest
import pathmagic  # noqa
from common.mongoclient import MyMongoClient
from src.main import FooClass
import logging
from common.log import log_init_console

logger = log_init_console(__name__, logging.DEBUG)


class TestMain(unittest.TestCase):

    def test_insert_person(self):
        url = 'mongodb://localhost:27017/test'
        target = FooClass(url)
        target.insert_person()
        client = MyMongoClient(url)
        result = client.find_one(collection_name='bar', filter={'name': 'George'})
        self.assertEqual(result['age'], '36')
        client.delete_one(collection_name='bar', key={'name': 'George'})


if __name__ == '__main__':
    unittest.main()
