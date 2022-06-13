#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : addReplay.py
#  Description : function to add a replay to the database
#
#  --
#
#  Last modification : 2022/4/16

# Import needed packages
from json import dumps, loads


# Import personal packages
from .. import connectDatabase
from ..GetFunctions.getReplays import getReplay, getPlayingReplaysId
from ..GetFunctions.getDailyReplay import getDailyReplay, getPlayingDailyReplaysId
from ..GetFunctions.getUsersConfig import getUsersConfig
from ...Core.Exceptions.ReplaysError import NoPlayingGameError
from ...Core.FormatData.formatReplays import formatReplays
from ...Core.insertReplay import insertReplay


def addReplay(id_user: int, neededWord: str, gameMode: str, replay: dict = None, word: str = None) -> None:
    """
    Function to add a replay to the database
    :param gameMode: the game mode
    :param word: the word that the user gave
    :param neededWord: the word that the user need to find
    :param id_user: id of the author of the replay
    :param replay: replay to add
    :return: None
    """
    try:
        oldReplayId = getPlayingReplaysId(id_user, gameMode, len(neededWord))
        oldReplay = getReplay(user_id=id_user, game_id=oldReplayId)
        formatedReplay = formatReplays(word, replay)
        newReplay, playingState = insertReplay(
            loads(oldReplay[1]),
            formatedReplay,
            word,
            neededWord,
            getUsersConfig(userId=id_user)[1]
        )
        query = """
        UPDATE Replays SET replay = ?, playingState = ?
        WHERE id = ? AND answerLength = ? AND gameMode = ?;"""
        args = (dumps(newReplay), playingState, oldReplayId, len(neededWord), gameMode)
    except NoPlayingGameError:
        query = """
        INSERT INTO Replays (user_id, replay, playingState, neededWord, answerLength, gameMode, maxTries)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        if gameMode == 'normal':
            args = (id_user, dumps({}),
                    "playing", neededWord,
                    len(neededWord),
                    gameMode,
                    getUsersConfig(userId=id_user)[1])
        elif gameMode == 'daily':
            args = (id_user, dumps({}),
                    "playing", neededWord,
                    len(neededWord),
                    gameMode,
                    6)

    db, cursor = connectDatabase()
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()


def addDailyReplay(id_user: int, neededWord: str, replay: dict = None, word: str = None) -> None:
    """
    Function to add a replay to the database
    :param word: the word that the user gave
    :param neededWord: the word that the user need to find
    :param id_user: id of the author of the replay
    :param replay: replay to add
    :return: None
    """
    try:
        oldReplayId = getPlayingDailyReplaysId(id_user)
        oldReplay = getDailyReplay(user_id=id_user, game_id=oldReplayId)
        formatedReplay = formatReplays(word, replay)
        config = getUsersConfig(userId=id_user)
        newReplay, playingState = insertReplay(loads(oldReplay[1]), formatedReplay, word, neededWord, config[1])
        query = """UPDATE ReplaysDaily SET replay = ?, playingState = ? WHERE id = ?;"""
        args = (dumps(newReplay), playingState, oldReplayId)
    except NoPlayingGameError:
        query = """
        INSERT INTO ReplaysDaily (user_id, replay, playingState)
        VALUES (?, ?, ?);
        """
        args = (id_user, dumps({}), "playing")

    db, cursor = connectDatabase()
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()
