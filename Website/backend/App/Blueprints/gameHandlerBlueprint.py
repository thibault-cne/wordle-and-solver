#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : gameHandlerBlueprint.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 18/04/2022 12:12

# Import needed packages
from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from typing import Tuple


# Import personal packages
from ..Core.GameHandlers.dailyGameHandler import handleDailyGameCreation, handleDailyWordTest
from ..Core.GameHandlers.normalGameHandler import handleGameCreation, handleConfigLoading, handleWordTest


# Define the blueprint
gameHandlerBlueprint = Blueprint('gameHandlerBlueprint', __name__)


@gameHandlerBlueprint.route('/game-api/<string:gameMode>/<string:method>', methods=['GET', 'POST'])
@jwt_required(optional=True)
def handleGame(gameMode: str, method: str) -> Tuple[Response, int]:
    """
    Handle the game
    :param gameMode: the game mode
    :param method: the method to call
    :return:
    """
    username = get_jwt_identity()
    if request.method == 'GET':
        if method == 'create':
            if gameMode == 'normal':
                requestPayload, statusCode = handleGameCreation(username)
            elif gameMode == 'daily':
                requestPayload, statusCode = handleDailyGameCreation(username)
            return jsonify(requestPayload), statusCode

        if method == "config":
            if gameMode == 'normal':
                configData, statusCode = handleConfigLoading(username)
            return jsonify(configData), statusCode

    if request.method == "POST":
        if method == "testWord":
            if gameMode == 'normal':
                liste_mot = request.json['mot']
                essai = request.json['essai']
                if username is None:
                    neededWord = request.json['neededWord']
                else:
                    neededWord = ""
                requestPayload, statusCode = handleWordTest(liste_mot, username, neededWord, essai)

            elif gameMode == 'daily':
                liste_mot = request.json['mot']
                essai = request.json['essai']
                requestPayload, statusCode = handleDailyWordTest(liste_mot, username, essai)

            return jsonify(requestPayload), statusCode
