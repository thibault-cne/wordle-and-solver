#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : louiscleriot
#   File : setListeTI.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 4/22/22, 12:07 PM
import json

from flask import jsonify

from .. import connectDatabase


def setListe(id_user: int, liste, id_game: int):
    j = 0
    dico = {}
    for i in liste:
        dico[j] = i
        j += 1
    j = 0
    db, cursor = connectDatabase()
    query = """UPDATE PartieTI SET liste_reponse=? WHERE userID=? AND id=?;"""
    args = (json.dumps(liste), id_user, id_game)
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()


def setFinParti(id_user: int, id_game: int):
    db, cursor = connectDatabase()
    query = """UPDATE PartieTI SET playingState=? WHERE userID=? AND id=?"""
    args = ("played", id_user, id_game)
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()


def setMotTI(id_user, id_game, mot, status, nbTries):
    dico = {}
    db, cursor = connectDatabase()
    query = """SELECT replay FROM PartieTI WHERE userId=? AND id =? AND playingState=?"""
    args = (id_user, id_game, "playing")
    cursor.execute(query, args)
    dicoc = cursor.fetchall()
    dicoc = json.loads(dicoc[0][0])
    for i in range(len(dicoc)):
        dico[str(i)] = {}
        dico[str(i)] = dicoc[str(i)]
    dico[str(nbTries)] = {}
    for i in range(len(mot)):
        dico[str(nbTries)][i] = {
            'letter': mot[i],
            'status': status[i]
        }
    query = """UPDATE PartieTI SET replay=? WHERE userID=? AND id=?"""
    args = (json.dumps(dico), id_user, id_game)
    cursor.execute(query, args)
    db.commit()
    cursor.close()
    db.close()
