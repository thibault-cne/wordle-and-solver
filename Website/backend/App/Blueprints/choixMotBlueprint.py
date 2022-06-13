#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : louischatard
#  File : lancerPartieBlueprint.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/12

from flask import request, session, Blueprint, jsonify, Response
from ..Core.choisir_mot import choisir_mot

LancerPartieBP = Blueprint("LancerPartieBP", __name__)


@LancerPartieBP.route("/grille", methods=['GET', 'POST'])
def commencer():
    if request.method == "GET":
        # a modif avec le nom donner par la config
        longueur = request.json['longueur']
        mot = choisir_mot(longueur)
        return jsonify({mot: 0}), 200
