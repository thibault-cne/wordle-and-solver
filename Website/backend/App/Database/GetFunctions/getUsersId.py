#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : getUsersId.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 19/04/2022 18:00

# Import needed packages


# Import personal packages
from .. import connectDatabase


def getUsersId(username: str) -> int:
    """
    Get the id of a user
    :param username: the username of the user
    :return: the id of the user
    """
    query = "SELECT id FROM Users WHERE username = ?"
    arg = (username,)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    usersId = cursor.fetchone()[0]
    db.close()
    return usersId
