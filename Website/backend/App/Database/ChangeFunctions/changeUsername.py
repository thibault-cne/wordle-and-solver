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
from ...Core.Exceptions.UsersErrors import UsernameAlreadyUsed
from ..CheckFunctions.checkUsers import checkUsers

def changeUsername(username: str, new_username: str) -> bool:
    """

    :param username: The user's username, new_username: the name the user wants to have by now
    :return: True if the new username is available or a UserNotFound error
    """
    userStatement = checkUsers(new_username)

    if not userStatement:
        query = """
                UPDATE Users
                SET username = ?
                WHERE Users.username = ? """
        arg = (new_username, username)

        db, cursor = connectDatabase()
        cursor.execute(query, arg)
        db.commit()
        cursor.close()
        db.close()

        return True

    else:
        raise UsernameAlreadyUsed
