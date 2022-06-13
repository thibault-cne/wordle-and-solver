#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : checkPlayingGame.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 20/04/2022 14:13

# Import needed packages


# Import personal packages
from ..GetFunctions.getUsersId import getUsersId
from .. import connectDatabase


def checkPlayingGame(username: str, wordLength: int, gameMode: str) -> bool:
    """
    Check if the user is playing a normal game
    :param gameMode:
    :param username: the username of the user
    :param wordLength: the length of the word
    :return: true if the user is playing a normal game, false otherwise
    """
    userId = getUsersId(username)

    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("""
        SELECT id FROM Replays
        WHERE user_id = ? AND playingState = ? AND answerLength = ? AND gameMode = ?""",
                   (userId, "playing", wordLength, gameMode))
    # Get the result
    result = cursor.fetchall()
    # Close the cursor
    cursor.close()
    # Close the connection
    db.close()

    return len(result) == 1
