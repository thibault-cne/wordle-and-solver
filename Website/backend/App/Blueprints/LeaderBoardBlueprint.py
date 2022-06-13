from flask import Blueprint, Response, jsonify, request


from App.Database.GetFunctions.getLeaderBoard import getLeaderBoard
from App.Database.GetFunctions.getUserName import getUserName

leaderBP = Blueprint("leaderBP", __name__)


@leaderBP.route("/leaderboard", methods=['GET'])
def Leader():
    leaderboard = getLeaderBoard()
    for i in range(len(leaderboard)):
        leaderboard[i] = list(leaderboard[i])
        leaderboard[i][0] = getUserName(leaderboard[i][0])

    leaderboard=tuple(leaderboard)


    return jsonify(leaderboard), 200
