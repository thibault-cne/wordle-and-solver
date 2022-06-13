#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : insertReplay.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/16

# Import needed packages
from typing import Union, Tuple


# Import personal packages
from .Exceptions.ReplaysError import GameHasEndedError


def insertReplay(data: dict, new_replay: dict, word: str, neededWord: str, maxTries: int) -> Union[Tuple[dict, str], None]:
    """
    Insert a replay in a dictionary
    :param word: the word the user has given
    :param maxTries: the maximum number of tries
    :param data: the dictionary
    :param new_replay: The new replay to insert
    :param neededWord: The users needed word
    :return: the dictionary with the new replay
    """
    maxTry = 0
    for i in data:
        maxTry = int(i)
    maxTry += 1

    if maxTry < maxTries and word != neededWord:
        data[maxTry] = new_replay
        return data, "playing"
    elif maxTry == maxTries or word == neededWord:
        data[maxTry] = new_replay
        return data, "ended"
    else:
        raise GameHasEndedError("The game has already ended")
