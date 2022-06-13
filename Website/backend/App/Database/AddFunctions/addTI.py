#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : louiscleriot
#   File : addTI.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 4/22/22, 11:36 AM
# Import needed packages
import json

from .. import connectDatabase


# Import personal packages


def addTI(id_user: int, replay: str, id):
    dico = {}
    dico['0']={}
    for i in range(len(replay)):
        dico['0'][i] = {
            'letter': replay[i],
            'status': id[i]
        }
    db, cursor = connectDatabase()
    query = """INSERT INTO PartieTI (userId, replay, playingState) VALUES (?,?,?)"""
    args = (id_user, json.dumps(dico), "playing")
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()
