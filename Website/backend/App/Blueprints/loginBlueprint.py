# Import needed packages
from flask import request, Blueprint, jsonify, Response
from typing import Tuple
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token


# Import personal packages
from ..Database.CheckFunctions.checkUsers import checkUsersPassword
from ..Database.AddFunctions.addUser import addUser
from ..Core.Exceptions.UsersErrors import UserNotFound, UsernameAlreadyUsed

loginBP = Blueprint("loginBP", __name__)


@loginBP.route('/auth-api/<string:method>', methods=['POST'])
def login(method: str) -> Tuple[Response, int]:
    # Check if request method is POST
    if request.method == 'POST':
        # Get the request data
        username = request.json['username']
        password = request.json['password']

        returnData = {
            'status': "failure",
            'access': None,
            'refresh': None}
        returnCode = 200

        if method == "login":
            try:
                userStatement = checkUsersPassword(username, password)

                if userStatement:
                    access_token = create_access_token(identity=username, fresh=True)
                    refresh_token = create_refresh_token(identity=username)

                    returnData['status'] = "success"
                    returnData['access'] = access_token
                    returnData['refresh'] = refresh_token

                    returnCode = 200

                else:
                    # Wrong users credentials
                    returnData['status'] = "failure"
                    returnData['error'] = "WrongPassword"

                    returnCode = 200

            except UserNotFound:
                # No user with this username
                returnData['status'] = "failure"
                returnData['error'] = "UserNotFound"

                returnCode = 200

        elif method == "register":
            try:
                addUser(username, password)

                access_token = create_access_token(identity=username, fresh=True)
                refresh_token = create_refresh_token(identity=username)

                returnData['status'] = "success"
                returnData['access'] = access_token
                returnData['refresh'] = refresh_token

                returnCode = 200

            except UsernameAlreadyUsed:
                # No user with this username
                returnData['status'] = "failure"
                returnData['error'] = "UsernameAlreadyUsed"

                returnCode = 200

        return jsonify(returnData), returnCode


# Route to refresh the token
@loginBP.route('/auth-api/refresh', methods=['GET'])
@jwt_required(refresh=True)
def refreshToken():
    if request.method == 'GET':
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user)
        return jsonify({"accessToken": new_token})


# Page pour se log out
@loginBP.route('/logout')
@jwt_required()
def logout():
    return jsonify({"status": "success"})
