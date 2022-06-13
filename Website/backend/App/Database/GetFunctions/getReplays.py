#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : getReplays.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/16

# Import needed packages
from typing import Tuple, List

# Import personal packages
from .. import connectDatabase
from ...Core.Exceptions.ReplaysError import GameIDNotFoundError, NoPlayingGameError
from ...Core.FormatData.formatReplays import formatRenderingReplays


def getReplay(user_id: int, game_id: int) -> Tuple[int, str, int]:
    """
    Get the replay of a game
    :param user_id:
    :param game_id:
    :return: list of replay
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("SELECT * FROM Replays WHERE user_id = ? AND id = ?", (user_id, game_id))
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


def getAllReplays(user_id: int) -> List:
    """
    Function to get all the replay of a user
    :param user_id: the user's id
    :return: the list of all the replay
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("SELECT replay, neededWord, maxTries FROM Replays WHERE user_id = ? AND playingState = 'ended'", (user_id,))
    # Get the result
    result = cursor.fetchall()

    # Close the cursor
    cursor.close()
    # Close the connection
    db.close()
    result = formatRenderingReplays(result)
    return result


def getPlayingReplaysId(user_id: int, gameMode: str, wordLength: int) -> int:
    """
    Get the replay of a game
    :param gameMode:
    :param wordLength: the length of the word
    :param user_id:
    :return: the playing game's id
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute("""SELECT id FROM Replays
                   WHERE user_id = ? AND playingState = ? AND answerLength = ? AND gameMode = ?""",
                   (user_id, "playing", wordLength, gameMode))
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


def getUsersCurrentWord(userId: int, wordLength: int) -> str:
    """
    Function to get the current word of a user
    :param userId: the user's id
    :param wordLength: the length of the word
    :return: the current word
    """
    # Connect to the database
    db, cursor = connectDatabase()
    # Execute the query
    cursor.execute(
        """SELECT neededWord FROM Replays
        WHERE user_id = ? AND playingState = 'playing' AND answerLength = ? AND gameMode = 'normal';""",
        (userId, wordLength))
    # Get the result
    result = cursor.fetchone()
    # Close the cursor
    cursor.close()
    # Close the connection
    db.close()
    try:
        assert len(result) == 1
        return result[0]
    except AssertionError:
        raise NoPlayingGameError(userId)
