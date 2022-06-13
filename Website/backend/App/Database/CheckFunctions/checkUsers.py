#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : checkUsers.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4

# Import needed packages
from werkzeug.security import check_password_hash


# Import personal packages
from ..GetFunctions.getUsersPassword import getUsersPassword
from ...Core.Exceptions.UsersErrors import UserNotFound, UsernameAlreadyUsed
from .. import connectDatabase


def checkUsersPassword(username: str, password: str) -> bool:
    """
    Function to check if the password of a user is correct
    :param username: the user's username
    :param password: the user's attempt for his password
    :return: True if the
    users has the right password or False if he hasn't and UserNotFound if there is no users with this username
    """
    try:
        cypherPassword = getUsersPassword(username)
        if check_password_hash(cypherPassword, password):
            return True
        else:
            return False

    except UserNotFound:
        raise UserNotFound


def checkUsers(username: str) -> bool:
    """
    Function to check if a user exists
    :param username: the user's username
    :return: True if the user's exist and return False if not.
    """
    query = """SELECT * FROM Users WHERE username = ?"""
    arg = (username,)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    cursor.close()
    db.close()

    if len(data) > 0:
        return True
    else:
        return False
