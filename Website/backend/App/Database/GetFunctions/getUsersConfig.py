#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : getUsersConfig.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 18/04/2022 15:25

# Import needed packages


# Import personal packages
from .. import connectDatabase



def getUsersConfig(username: str = None, userId: int = None) -> dict:
    """
    Get the configuration of a user
    :param userId:
    :param username: The username of the user
    :return: The configuration of the user
    """
    db, cursor = connectDatabase()
    if username is not None:
        query = """
            SELECT wordLength, maxTries
            FROM Config JOIN Users ON Config.id = Users.id
            WHERE username = ?
        """
        arg = (username,)
    elif userId is not None:
        query = """
            SELECT wordLength, maxTries
            FROM Config JOIN Users ON Config.id = Users.id
            WHERE Users.id = ?
        """
        arg = (userId,)
    cursor.execute(query, arg)
    result = cursor.fetchone()
    db.close()
    return result
