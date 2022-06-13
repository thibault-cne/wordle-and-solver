import json

from flask import request, session, Blueprint, jsonify, Response
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..Core.wordleTIC import wordle_ti
from ..Core.ExistenceMot import ExistenceMot
import os

from ..Database.AddFunctions.addTI import addTI
from ..Database.CheckFunctions.checkPlayingGameTI import checkPlayingGameTI
from ..Database.GetFunctions.GetTI import getList, getplayingListId, getParti, getPlayingPartiId
from ..Database.GetFunctions.getMaxTries import getMaxTries
from ..Database.GetFunctions.getUsersConfig import getUsersConfig
from ..Database.GetFunctions.getUsersId import getUsersId
from ..Database.SetFunctions.setListeTI import setListe, setFinParti, setMotTI

VerifMotTIBP = Blueprint("VerifMotTIBP", __name__)


@VerifMotTIBP.route("/testTI", methods=['POST'])
@jwt_required()
def testTI():
    if request.method == "POST":
        username = get_jwt_identity()
        liste_mot = request.json['mot']
        nbTries = request.json['essai']
        nb_essais_choisis = getMaxTries(username=username)
        mot = ""
        for i in liste_mot:
            mot += i['lettre']
        victoire = ""
        for i in range(len(mot)):
            victoire += "2"
        if ExistenceMot(mot.lower()):
            if nbTries == 0:
                with open(os.path.abspath("../backend/Data/Text/l_" + str(len(mot)) + "_reponse.txt"), "r") as file:
                    possibility = file.readlines()
                retourfonction = wordle_ti(mot, possibility)
                addTI(getUsersId(username), mot, retourfonction["id"])
                partiID = getPlayingPartiId(getUsersId(username))
                setListe(getUsersId(username), retourfonction["liste"], partiID)
            elif nbTries <= nb_essais_choisis:
                possibility = getList(getUsersId(username), getplayingListId(getUsersId(username)))
                retourfonction = wordle_ti(mot, possibility)
                partiID = getPlayingPartiId(getUsersId(username))
                setListe(getUsersId(username), retourfonction["liste"], partiID)
                setMotTI(getUsersId(username), partiID, mot, retourfonction["id"], nbTries)
                if retourfonction["id"] == victoire:
                    setFinParti(getUsersId(username), partiID)
                    return jsonify(retourfonction["id"], {"status": "win"}, {"message": ""}), 200
                if nbTries + 1 == nb_essais_choisis and retourfonction["id"] != victoire:
                    setFinParti(getUsersId(username), partiID)
                    return jsonify(retourfonction["liste"], {"status": "perdu"},
                                   {"message": "il restait : " + str(len(retourfonction["liste"])) + "mot"})
            return jsonify(retourfonction["id"], {"status": "existe"}, {"message": ""}), 200
        else:
            return jsonify("", {"status": "inconnu"}, {"message": ""})


@VerifMotTIBP.route("/<string:method>", methods=['GET'])
@jwt_required()
def generegrille(method):
    username = get_jwt_identity()
    if method == "create":
        requestPayload = {
            'status': "success",
            'hasPendingGame': False
        }
        if checkPlayingGameTI(username):
            requestPayload['hasPendingGame'] = True
            requestPayload['pendingGame'] = json.loads(getParti(
                getUsersId(username),
                getPlayingPartiId(getUsersId(username))
            ))
        return jsonify(requestPayload), 200
    if method == "config":
        config = getUsersConfig(username)
        configData = {
            "config": {
                "nbLetter": config[0],
                "nbTries": config[1],
            },
            "status": "success"
        }
        statusCode = 200
        return jsonify(configData), statusCode
