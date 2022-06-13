#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : normalGameHandler.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 25/04/2022 16:56

# Import needed packages
import json
from werkzeug.security import generate_password_hash
from typing import Tuple


# Import personal packages
from ..ExistenceMot import ExistenceMot
from ..choisir_mot import choisir_mot
from ..coreScore import scoreGame
from ..retrieveCypherWord import retrieveCypherWord
from ..verfi_mot import verif_mot
from ...Database.AddFunctions.addReplay import addReplay
from ...Database.CheckFunctions.checkPlayingGame import checkPlayingGame
from ...Database.GetFunctions.getMaxTries import getMaxTries
from ...Database.GetFunctions.getReplays import getPlayingReplaysId, getReplay, getUsersCurrentWord
from ...Database.GetFunctions.getUsersConfig import getUsersConfig
from ...Database.GetFunctions.getUsersId import getUsersId


def handleGameCreation(username: str) -> Tuple[dict, int]:
    requestPayload = {
        'status': "success",
        'hasPendingGame': False
    }
    if username is not None:
        config = getUsersConfig(username=username)
        if checkPlayingGame(username, config[0], "normal"):
            requestPayload['hasPendingGame'] = True
            requestPayload['pendingGame'] = json.loads(getReplay(
                getUsersId(username),
                getPlayingReplaysId(getUsersId(username), wordLength=config[0], gameMode="normal")
            )[1])
        else:
            word = choisir_mot(getUsersConfig(username=username)[0])
            addReplay(id_user=getUsersId(username), neededWord=word, gameMode="normal")
    else:
        word = choisir_mot(5)
        requestPayload['config'] = {
            "word": generate_password_hash(word, "sha256"),
        }
    return requestPayload, 200


def handleConfigLoading(username: str) -> Tuple[dict, int]:
    if username is not None:
        config = getUsersConfig(username=username)
        configData = {
            "config": {
                "nbLetter": config[0],
                "nbTries": config[1],
            },
            "status": "success"
        }
        statusCode = 200
    else:
        configData = {
            "config": {
                "nbLetter": 5,
                "nbTries": 6,
            },
            "status": "success"
        }
        statusCode = 200

    return configData, statusCode


def handleWordTest(liste_mot: dict, username: str, neededWord: str, essai: int) -> Tuple[dict, int]:
    mot = ""
    for i in liste_mot:
        mot += i['lettre']
    mot = mot.lower()
    if username is not None:
        motADeviner = getUsersCurrentWord(getUsersId(username), len(mot))
    else:
        motADeviner = retrieveCypherWord(neededWord)
    nb_essais_choisis = getMaxTries(username=username)

    if ExistenceMot(mot):
        returnData = verif_mot(motADeviner, mot, essai + 1, nb_essais_choisis)
        if username is not None:
            addReplay(
                id_user=getUsersId(username),
                replay=returnData,
                word=mot,
                neededWord=motADeviner,
                gameMode="normal"
            )
        if mot == motADeviner:
            returnData['status'] = "win"
            if username is not None:
                scoreGame(len(mot), essai, nb_essais_choisis, getUsersId(username))
            return returnData, 200
        return verif_mot(motADeviner, mot, essai + 1, nb_essais_choisis), 200
    return {"status": "inconnu"}, 200
