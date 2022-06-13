#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : louis chatard
#  File : changeUsername.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/17

# Import needed packages


# Import personal packages
from .. import connectDatabase
from ...Core.Exceptions.UsersErrors import UserNotFound


def changePassword(username: str, new_password: str) -> bool:
    """

    :param username: The user's username, new_username: the name the user wants to have by now
    :return: True if the new username is available or a UserNotFound error
    """
    query = """
            UPDATE Users
            SET password = ?
            WHERE Users.username = ? """
    arg = (new_password, username)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    db.commit()
    cursor.close()
    db.close()

    return True
