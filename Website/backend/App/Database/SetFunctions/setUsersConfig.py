#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : setUsersConfig.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 19/04/2022 17:57

# Import needed packages


# Import personal packages
from .. import connectDatabase
from ..GetFunctions.getUsersId import getUsersId



def setUsersConfig(username: str, config: dict) -> None:
    """
    Set the config of the user
    :param username: the username of the user
    :param config: the config to set
    :return:
    """
    usersId = getUsersId(username)
    queryConfig = """UPDATE Config SET wordlength = ?, maxTries = ? WHERE id = ?"""
    args = (config['wordLength'], config['maxTries'], usersId)

    db, cursor = connectDatabase()
    cursor.execute(queryConfig, args)
    db.commit()
    db.close()
    return
