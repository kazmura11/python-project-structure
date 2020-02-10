# coding: utf-8
import os
import pathmagic  # noqa
from common.mongoclient import MyMongoClient
from common.log import log_init_console_file
import logging

logpath = os.path.join(os.path.dirname(__file__), 'main.log')
logger = log_init_console_file(__name__, logging.INFO, logpath)


class FooClass:
    
    def __init__(self, url):
        self.client = MyMongoClient(url)
    
    def insert_person(self):
        self.client.insert_one(collection_name='bar', value={'name': 'George', 'age': '36'})


if __name__ == '__main__':
    foo = FooClass('mongodb://localhost:27017/test')
