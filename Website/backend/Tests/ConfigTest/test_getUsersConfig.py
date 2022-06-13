#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : test_getUsersConfig.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 19/04/2022 17:31

# Import needed packages


# Import personal packages
from backend.App.Database.GetFunctions.getUsersConfig import getUsersConfig


def test_get_users_config():
    config = getUsersConfig("Test")

    assert config[0] == 5
    assert config[1] == 6
    assert config[2] == 1.0
