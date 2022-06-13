#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : configBlueprint.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/12

# Import needed packages
from flask import Blueprint, Response, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from typing import Tuple

# Import personal packages
from ..Database.SetFunctions.setUsersConfig import setUsersConfig


configBP = Blueprint("configBP", __name__)


@configBP.route("/config-api/<string:config_name>", methods=['POST'])
@jwt_required()
def get_config(config_name: str) -> Tuple[Response, int]:
    """
    Modify the configuration of the website
    :param config_name: The config to modify
    :return: The statement if the configuration has been updated
    """
    if request.method == "POST":
        if config_name == "set":
            setUsersConfig(get_jwt_identity(), {
                'wordLength': int(request.json['wordLength']),
                'maxTries': int(request.json['maxTries'])
            })

            return jsonify({"success": True}), 200
