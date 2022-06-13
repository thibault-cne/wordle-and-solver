#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : test_insertReplay.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/16


# Import personal packages
from backend.App.Core.insertReplay import insertReplay
from backend.App.Core.Exceptions.ReplaysError import GameHasEndedError



def test_insert_replay():
    data = {
        1: "tests",
        2: "tusmo"
    }

    newData = insertReplay(data, "testo")

    assert newData[0][3] == "testo"
    assert newData[1] == "playing"

    data = {
        1: "tests",
        2: "tusmo",
        3: "testo",
        4: "testo",
        5: "testo",
        6: "testo"
    }

    try:
        _ = insertReplay(data, "testo")
        assert False
    except GameHasEndedError:
        assert True
