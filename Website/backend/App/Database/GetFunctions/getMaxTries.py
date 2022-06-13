#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : getMaxTries.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 18/04/2022 19:59

# Import needed packages


# Import personal packages
from .. import connectDatabase


def getMaxTries(username: str = None) -> int:
    """
    Get the max tries of a user
    :param username: the username of the user
    :return: the max tries of the user
    """
    if username:
        query = """SELECT maxTries FROM Config JOIN Users ON Config.id = Users.id WHERE Users.username = ?;"""
        arg = (username, )

        db, cursor = connectDatabase()
        cursor.execute(query, arg)
        data = cursor.fetchone()
        db.close()

        return data[0]

    else:
        return 6
