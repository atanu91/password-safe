import re


def validate_policy(password):
    """
    Please note password :
        1. Should have at least one number.
        2. Should have at least one uppercase and one lowercase character.
        3. Should have at least one special symbol.
        4. Should be between 8 to 20 characters long.
    :param password:
    :return: True or False
    """
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"

    # compiling regex
    pattern = re.compile(reg)

    # searching regex
    match_result = re.search(pattern, password)

    # validating conditions
    if match_result:
        # valid password with respect to policy
        return True
    else:
        # password not complaint with policy
        return False
