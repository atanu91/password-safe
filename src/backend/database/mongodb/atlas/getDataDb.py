import pymongo
import yaml

# extract configuration secrets from configuration file
# dbConfig.yml should be created taking dbConfig_template.yml as reference
with open('dbConfig.yml', 'r') as stream:
    db_config_object = yaml.safe_load(stream)

db_header = db_config_object['Connection']['header']
db_user_name = db_config_object['Connection']['user_name']
db_user_pass = db_config_object['Connection']['user_passwrd']
db_cluster = db_config_object['Connection']['cluster']
db_default_db = db_config_object['Connection']['default_db']
db_trailer = db_config_object['Connection']['trailer']

# prepare db connection string
db_connection_string = db_header + db_user_name + ":" + db_user_pass + db_cluster + "/" + db_default_db + db_trailer

# connect to MongoDb Atlas
client = pymongo.MongoClient(db_connection_string)
# get db object
# use db = client.list_database_names() to extract the list of databases
db = client.sample_analytics

# get collection object
collection = db.customers

print(collection.find_one())
