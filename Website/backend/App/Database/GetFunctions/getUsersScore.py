#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : getUsersScore.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 28/04/2022 17:03

# Import needed packages


# Import personal packages
from .. import connectDatabase


def getUsersScore(userId: int) -> int:
    query = """SELECT score FROM Leaderboard WHERE id = ?;"""
    args = (userId,)

    db, cursor = connectDatabase()
    cursor.execute(query, args)
    result = cursor.fetchone()
    db.close()
    return result[0]

