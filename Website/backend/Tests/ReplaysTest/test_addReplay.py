#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : test_addReplay.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/16

# Import needed packages
import json


# Import personal packages
from backend.App.Database import connectDatabase
from backend.App.Database.AddFunctions.addReplay import addReplay


def test_add_replay():
    deleteTestReplay()
    addReplay(999, "test", "chat")

    data, json_data = getTestReplay()

    assert len(data) == 1
    assert json_data == {}

    addReplay(999, "test", "chat")

    data, json_data = getTestReplay()

    assert len(data) == 1
    assert json_data['1'] == "test"

    deleteTestReplay()


def getTestReplay():
    db, cursor = connectDatabase()
    cursor.execute("SELECT * FROM Replays WHERE user_id = 999")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data, json.loads(data[0][1])


def deleteTestReplay():
    db, cursor = connectDatabase()
    cursor.execute("DELETE FROM Replays WHERE user_id = 999")
    db.commit()
    cursor.close()
    db.close()
