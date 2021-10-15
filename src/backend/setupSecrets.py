import string
import secrets
import yaml


def generate_encryption_secret():
    """Generates secret global encryption key for password"""
    # extract configuration secrets from configuration file
    # secretsConfig.yml should be created taking secretsConfig_template.yml as reference
    with open('src/backend/secretsConfig_template.yml', 'r') as stream_read:
        secrets_config_object_read = yaml.safe_load(stream_read)

    secrets_config_object_write = secrets_config_object_read

    c = string.ascii_letters + string.digits + string.punctuation
    # generate secret global encryption key
    secret_key = ''.join(secrets.choice(c) for i in range(32))

    secrets_config_object_write['Configuration']['encryption']['global'] = str(secret_key)

    # write the configuration secret to configuration file
    with open('src/backend/secretsConfig.yml', 'w') as stream_write:
        yaml.dump(secrets_config_object_write, stream_write)
