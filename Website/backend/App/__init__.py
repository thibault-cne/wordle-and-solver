#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : __init__.py
#  Description : File to config the web app
#
#  --
#
#  Last modification : 2022/3/31

# Import needed packages
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
from webargs.flaskparser import parser

# Import personal packages


# Definition of the app
def create_app() -> Flask:
    """
    Create the flask app
    :return: the flask app
    """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'jOQiU7q9I2l4eycgKM3hh6oTy7CEaX6j'

    # Config upload folder
    app.config['UPLOAD_FOLDER'] = "./Data/ProfilPictures/"

    # JWT Configuration
    app.config["JWT_SECRET_KEY"] = "VSfa4AP9UHqdM00NWXs0N3KgxoAeOZXK"
    app.config["JWT_HEADER_TYPE"] = "Bearer"
    app.config["JWT_TOKEN_LOCATION"] = "headers"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

    # Import blueprints
    from .Blueprints.loginBlueprint import loginBP
    app.register_blueprint(loginBP)
    from .Blueprints.configBlueprint import configBP
    app.register_blueprint(configBP)
    from .Blueprints.gameHandlerBlueprint import gameHandlerBlueprint
    app.register_blueprint(gameHandlerBlueprint)
    from .Blueprints.VerifMotTI_blueprint import VerifMotTIBP
    app.register_blueprint(VerifMotTIBP)
    from .Blueprints.profilBlueprint import profilBP
    app.register_blueprint(profilBP)
    from .Blueprints.LeaderBoardBlueprint import leaderBP
    app.register_blueprint(leaderBP)

    # Handle JWT with the app to enable authentication
    JWTManager(app)

    # Handle CORS with the app
    CORS(app, ressources={r'/*': {'origins': '*'}})

    return app
