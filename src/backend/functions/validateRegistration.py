import src.backend.functions.passwordPolicy as passwordPolicy
import src.backend.database.mongodb.atlas.interactDb as interactDb
from src.backend.database.mongodb.atlas.configureDb import db_api_collection_cred, password_safe_db


def validate_user_registration(username, password):
    """
    checks is user name already exists and if username and password conforms to password policy.
    :param username: the input username
    :param password: the input password
    :return: result as string
    """
    db_object = interactDb.connect(password_safe_db, db_api_collection_cred)
    collection_object = interactDb.InteractUser(db_object['collection'])
    user_query = dict({"user_name": username})
    # check if user name already exists
    if collection_object.get_data(user_query):
        return "Username taken. Please choose another username"
    else:
        if len(username) >= 4:
            pass
        else:
            return "Username should have at least 4 characters"

    pass_check = passwordPolicy.validate_policy(password)
    if pass_check:
        # passed password policy check
        pass
    else:
        # did not pass password policy check
        return "Password did not pass password policy"
