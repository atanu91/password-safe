import os
import yaml

# look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))
# preparing file path to be operating system agnostic
secrets_file_path = os.path.join(absolute_path, 'dbConfig.yml')

# extract configuration secrets from configuration file
# dbConfig.yml should be created taking dbConfig_template.yml as reference
with open(secrets_file_path, 'r') as stream:
    db_config_object = yaml.safe_load(stream)

db_header = db_config_object['Connection']['header']
db_user_name = db_config_object['Connection']['user_name']
db_user_pass = db_config_object['Connection']['user_passwrd']
db_cluster = db_config_object['Connection']['cluster']
db_default_db = db_config_object['Connection']['default_db']
db_trailer = db_config_object['Connection']['trailer']

# prepare db connection string
db_connection_string = db_header + db_user_name + ":" + db_user_pass + db_cluster + "/" + db_default_db + db_trailer

db_api_db_list = db_config_object['Database Group']['database']
# print(db_api_db_list)
for db_api_db_detail in db_api_db_list:
    db_api_db_name = db_api_db_detail['name']
    if db_api_db_name == "sample_db":
        password_safe_db = db_api_db_name
        db_collections = db_api_db_detail['collections']
        for db_collection_detail in db_collections:
            if db_collection_detail['type'] == "credentials":
                db_api_collection_cred = db_collection_detail['collection']


# print(password_safe_db)
# print(db_api_collection_cred)
