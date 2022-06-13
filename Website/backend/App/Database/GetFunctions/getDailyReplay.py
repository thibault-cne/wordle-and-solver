#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : getDailyReplay.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 25/04/2022 17:34

# Import needed packages
from typing import Tuple


# Import personal packages
from App.Core.Exceptions.ReplaysError import GameIDNotFoundError, NoPlayingGameError
from App.Database import connectDatabase


def getDailyReplay(user_id: int, game_id: int) -> Tuple[int, str, int]:
    """
    Get the replay of a game
    :param user_id: the user's id
    :param game_id: the game's id
    :return: list of replay
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("SELECT * FROM ReplaysDaily WHERE user_id = ? AND id = ?", (user_id, game_id))
    # Get the result
    result = cursor.fetchall()
    # Close the cursor
    cursor.close()
    # Close the connection
    db.close()
    try:
        assert len(result) == 1
        return result[0]
    except AssertionError:
        raise GameIDNotFoundError(game_id)


def getPlayingDailyReplaysId(user_id: int) -> int:
    """
    Get the replay of a game
    :param user_id: the user's id
    :return: the playing game's id
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("SELECT id FROM ReplaysDaily WHERE user_id = ? AND playingState = ?",
                   (user_id, "playing"))
    # Get the result
    result = cursor.fetchall()
    # Close the cursor
    cursor.close()
    # Close the connection
    db.close()
    try:
        assert len(result) == 1
        return result[0][0]
    except AssertionError:
        raise NoPlayingGameError(user_id)
