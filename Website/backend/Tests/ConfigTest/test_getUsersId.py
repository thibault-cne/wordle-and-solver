#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : test_getUsersId.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 19/04/2022 18:14

# Import needed packages


# Import personal packages
from backend.App.Database.GetFunctions.getUsersId import getUsersId


def test_get_users_id():
    userId = getUsersId("Test")

    assert userId == 2
