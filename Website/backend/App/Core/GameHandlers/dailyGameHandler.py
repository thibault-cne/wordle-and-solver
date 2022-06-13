#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : dailyGameHandler.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 25/04/2022 17:00

# Import needed packages
from typing import Tuple
import json


# Import personal packages
from App.Core.ExistenceMot import ExistenceMot
from App.Core.coreScore import scoreGame
from App.Core.coreDailyWord import getDailyWord
from App.Core.verfi_mot import verif_mot
from App.Database.AddFunctions.addReplay import addReplay
from App.Database.CheckFunctions.checkPlayingGame import checkPlayingGame
from App.Database.GetFunctions.getReplays import getReplay, getPlayingReplaysId
from App.Database.GetFunctions.getUsersId import getUsersId


def handleDailyGameCreation(username: str) -> Tuple[dict, int]:
    word = getDailyWord()
    requestPayload = {
        'status': "success",
        'hasPendingGame': False,
        'wordLength': len(word)
    }
    if username is not None:
        if checkPlayingGame(username, len(word), "daily"):
            requestPayload['hasPendingGame'] = True
            requestPayload['pendingGame'] = json.loads(getReplay(
                getUsersId(username),
                getPlayingReplaysId(getUsersId(username), gameMode="daily", wordLength=len(word))
            )[1])
        else:
            addReplay(id_user=getUsersId(username), neededWord=word, gameMode="daily")
    return requestPayload, 200


def handleDailyWordTest(liste_mot: dict, username: str, essai: int) -> Tuple[dict, int]:
    mot = ""
    for i in liste_mot:
        mot += i['lettre']
    mot = mot.lower()
    if username is not None:
        motADeviner = getDailyWord()
    else:
        motADeviner = getDailyWord()
    nb_essais_choisis = 6

    if ExistenceMot(mot):
        returnData = verif_mot(motADeviner, mot, essai + 1, nb_essais_choisis)
        if username is not None:
            addReplay(
                id_user=getUsersId(username),
                replay=returnData,
                word=mot,
                neededWord=motADeviner,
                gameMode="daily"
            )
        if mot == motADeviner:
            returnData['status'] = "win"
            if username is not None:
                scoreGame(len(mot), essai, nb_essais_choisis, getUsersId(username))
            return returnData, 200
        return verif_mot(motADeviner, mot, essai + 1, nb_essais_choisis), 200
    return {"status": "inconnu"}, 200
