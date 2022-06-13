#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : louiscleriot
#   File : GetTI.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 4/22/22, 11:50 AM
import json

from .. import connectDatabase


def getList(user_id: int, game_id: int):
    db, cursor = connectDatabase()
    query = """SELECT liste_reponse FROM PartieTI WHERE userId=? AND id=?"""
    args = (user_id, game_id)
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return json.loads(result[0][0])


def getplayingListId(user_id: int):
    db, cursor = connectDatabase()
    query = """SELECT id FROM PartieTI WHERE userId=? AND playingState=?"""
    args = (user_id, "playing")
    cursor.execute(query, args)
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0]


def getParti(user_id: int, game_id: int):
    db, cursor = connectDatabase()
    cursor.execute("SELECT replay FROM PartieTI WHERE userId = ? AND id = ?", (user_id, game_id))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    print(result)
    return result[0][0]

def getPlayingPartiId(user_id: int):
    db, cursor = connectDatabase()
    cursor.execute("SELECT id FROM PartieTI WHERE userId = ? AND playingState = ?", (user_id, "playing"))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result[0][0]
