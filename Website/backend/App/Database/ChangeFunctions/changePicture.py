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


def getUsersPicture(username: str, new_picture_path: str) -> bool:
    """

    :param username: The user's username, new_username: the name the user wants to have by now
    :return: True if the new username is available or a UserNotFound error
    """
    query = """
            UPDATE Users
            SET picture = ?
            WHERE Users.username = ? """
    arg = (new_picture_path, username)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return new_picture_path
    if len(data) > 0:
        return data[0][0]
    else:
        raise UserNotFound
