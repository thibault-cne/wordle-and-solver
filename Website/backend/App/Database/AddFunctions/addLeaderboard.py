#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : addLeaderboard.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 28/04/2022 16:55

# Import needed packages


# Import personal packages
from .. import connectDatabase
from ..GetFunctions.getUsersScore import getUsersScore


def addScore(score: int, userId: int) -> None:
    """
    Add a score to the leaderboard
    :param score: The score to add
    :param userId: The user's id
    :return: True if the score has been added
    """
    oldScore = getUsersScore(userId)
    query = """
        UPDATE Leaderboard SET score = ? WHERE id = ?;
    """
    args = (oldScore + score, userId)

    db, cursor = connectDatabase()
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()
