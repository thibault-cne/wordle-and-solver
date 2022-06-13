#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : louis chatard
#  File : getUsersPicture.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/17

# Import needed packages


# Import personal packages
from .. import connectDatabase
from ...Core.Exceptions.UsersErrors import UserNotFound


def getUsersPicture(username: str) -> str:
    """

    :param username: The user's username
    :return: the path to the picture of the user of the user or a UserNotFound error
    """
    query = """SELECT picture FROM Users WHERE username = ?"""
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
