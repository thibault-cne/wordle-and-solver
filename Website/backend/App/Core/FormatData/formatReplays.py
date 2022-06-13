#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : formatReplays.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 22/04/2022 17:04

# Import needed packages
import json
from typing import List


# Import personal packages


def formatReplays(word: str, wordStatement: dict) -> dict:
    returnData = {}

    for i in range(len(word)):
        returnData[i] = {
            'letter': word[i],
            'status': wordStatement[str(i)]
        }

    return returnData


def formatRenderingReplays(replayList: List) -> List:
    for i in range(len(replayList)):
        tempTuple = replayList[i]
        replayList[i] = (json.loads(tempTuple[0]), tempTuple[1], tempTuple[2])

    return replayList
