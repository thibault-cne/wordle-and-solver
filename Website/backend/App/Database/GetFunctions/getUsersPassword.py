#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : getUsersPassword.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4

# Import needed packages


# Import personal packages
from .. import connectDatabase
from ...Core.Exceptions.UsersErrors import UserNotFound


def getUsersPassword(username: str) -> str:
    """
    Get the password of a user
    :param username: The user's username
    :return: the password of the user or a UserNotFound error
    """
    query = """SELECT password FROM Users WHERE username = ?"""
    arg = (username,)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    cursor.close()
    db.close()

    if len(data) > 0:
        return data[0][0]
    else:
        raise UserNotFound
