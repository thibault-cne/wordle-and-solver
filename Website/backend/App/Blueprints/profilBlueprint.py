# Import needed packages
from PIL import Image
from flask import request, Blueprint, jsonify, Response, current_app, send_file
from typing import Tuple
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash


# Import personal packages
from ..Core.coreImages import save_candidate_picture, readImage
from ..Database.ChangeFunctions.changePassword import changePassword
from ..Database.ChangeFunctions.changeUsername import changeUsername
from ..Database.GetFunctions.getUsersId import getUsersId
from ..Database.GetFunctions.getReplays import getAllReplays
from ..Database.CheckFunctions.checkUsers import checkUsers

profilBP = Blueprint("profilBP", __name__)


@profilBP.route('/profil-api/<string:method>', methods=['GET', 'POST'])
@jwt_required()
def profil(method: str) -> Tuple[Response, int]:
    username = get_jwt_identity()

    if request.method == 'GET':
        if method == 'getinfo':
            returnData = {'username': username, 'status': "succes"}
            return jsonify(returnData), 200

        elif method == 'getPicture':
            img = readImage(username, current_app.config['UPLOAD_FOLDER'])
            return send_file(img, mimetype='image/*'), 200

        elif method == 'getReplays':
            returnData = {'status': "success"}
            result = getAllReplays(getUsersId(username))
            returnData['replays'] = result
            return jsonify(returnData), 200

    if request.method == 'POST':
        if method == 'changePicture':
            img = Image.open(request.files['image'])
            save_candidate_picture(username, current_app.config['UPLOAD_FOLDER'], img)
            return jsonify({'status': "success"}), 200


            
        if method == 'changeUsername':
            new_username = request.json['new_username']
            userStatement = checkUsers(new_username)
            if not userStatement:
                changeUsername(username, new_username)
                access_token = create_access_token(identity=new_username)
                refresh_token = create_refresh_token(identity=new_username)
                returnData = {'status': "success",}
                returnData['access'] = access_token
                returnData['refresh'] = refresh_token
                returnCode = 200
            elif userStatement:
                returnData = {'status': "alreadyUsedUsername",}
                returnCode = 200          
            return jsonify(returnData), returnCode

        if method == 'changePassword':
            new_password = request.json['password']
            cipherPassword = generate_password_hash(new_password)
            changePassword(username, cipherPassword)
            returnData = {'status': "success",}
            returnCode = 200
            return jsonify(returnData), returnCode
            
