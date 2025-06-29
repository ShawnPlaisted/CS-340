from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Crud:
    def __init__(self, username, password):
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
        self.database = self.client['AAC']

    def create(self, data):
        if data:
            self.database.animals.insert_one(data)
            return True
        return False

    def read(self, query):
        return list(self.database.animals.find(query))

    def update(self, query, new_values):
        if query and new_values:
            result = self.database.animals.update_many(query, {'$set': new_values})
            return result.modified_count
        return 0

    def delete(self, query):
        if query:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        return 0