#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : louiscleriot
#   File : checkPlayingGameTI.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 4/25/22, 8:20 PM
from ..GetFunctions.getUsersId import getUsersId
from .. import connectDatabase

def checkPlayingGameTI(username: str) -> bool:
    userId = getUsersId(username)
    db, cursor = connectDatabase()
    cursor.execute("SELECT id FROM PartieTI WHERE userId = ? AND playingState = ?", (userId, "playing"))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return len(result) == 1
