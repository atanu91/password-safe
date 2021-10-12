from src.backend.database.mongodb.atlas.configureDb import db_connection_string
import pymongo

# perform client connection
db_client = pymongo.MongoClient(db_connection_string)


def connect(database, collection):
    """performs db connection and returns a dictionary of database and collection object"""
    db = db_client.get_database(database)
    collection = db.get_collection(collection)
    return {"db": db, "collection": collection}


class InteractUser:
    """MongoDb atlas class comprising of all the possible database operations"""

    def __init__(self, collection):
        self.collection = collection

    def get_data(self, user_name):
        """performs data extraction"""
        user_details = self.collection.find_one({"user_name": user_name})
        return user_details

    def insert_data(self, query):
        """performs data insert"""
        return ""

    def delete_data(self, query):
        """performs removal of data"""
        return ""

    def update_data(self, query):
        """performs data update"""
        return ""
