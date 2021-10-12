from configureDb import db_connection_string
import pymongo

# connect to MongoDb Atlas
db_connect_client = pymongo.MongoClient(db_connection_string)
# get db object
# use db = client.list_database_names() to extract the list of databases
db_list = db_connect_client.list_database_names()
if "users" in db_list:
    print("The database exists.")
print("The database does not exists")
