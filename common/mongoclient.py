from pymongo import MongoClient
from logging import getLogger

logger = getLogger(__name__)


class MyMongoClient:
    """[summary]
    MongoDB CRUD Utility
    """
    def __init__(self, url):
        """[summary]
        Constructor
        Args:
            url ([string]): [url]
        """
        self.db = MongoClient(url).get_default_database()

    def drop_collection(self, collection_name):
        self.db.drop_collection(collection_name)

    def find_one(self, collection_name, filter, sort=[]):
        collection = self.db[collection_name]
        return collection.find_one(filter, sort=sort)

    def insert_one(self, collection_name, value):
        collection = self.db[collection_name]
        return collection.insert_one(value)

    def delete_one(self, collection_name, key):
        collection = self.db[collection_name]
        return collection.delete_one(key)
