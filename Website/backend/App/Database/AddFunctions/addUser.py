#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : addUser.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4

# Import needed packages
from werkzeug.security import generate_password_hash


# Import personal packages
from .. import connectDatabase
from ..CheckFunctions.checkUsers import checkUsers
from ...Core.Exceptions.UsersErrors import UsernameAlreadyUsed


def addUser(username: str, password: str) -> bool:
    """

    :param username: the new user's username
    :param password: the new user's clear password
    :return: returns True if the user has been added or raises UsernameAlreadyUsed.
    """
    userStatement = checkUsers(username)

    if not userStatement:
        cypherPassword = generate_password_hash(password, "sha256")

        query_user = """INSERT INTO Users (username, password) VALUES (?, ?);"""
        query_config = """INSERT INTO Config (wordlength, maxTries) VALUES (5, 6);"""
        query_leaderboard = """INSERT INTO Leaderboard (score) VALUES (0);"""
        args = (username, cypherPassword)

        db, cursor = connectDatabase()
        cursor.execute(query_user, args)
        cursor.execute(query_config)
        cursor.execute(query_leaderboard)
        db.commit()
        cursor.close()
        db.close()

        return True

    else:
        raise UsernameAlreadyUsed
