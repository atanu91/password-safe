import os
import yaml

# look for your absolute directory path
absolute_path = os.path.dirname(os.path.abspath(__file__))
# preparing file path to be operating system agnostic
secrets_file_path = os.path.join(absolute_path, 'secretsConfig.yml')

# extract configuration secrets from configuration file
# secretsConfig.yml should be created taking secretsConfig_template.yml as reference
with open(secrets_file_path, 'r') as stream:
    secrets_config_object = yaml.safe_load(stream)

secret_key = secrets_config_object['Configuration']['encryption']['global']

# print(secret_key)
