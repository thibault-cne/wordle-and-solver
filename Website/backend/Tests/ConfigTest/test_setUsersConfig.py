#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : test_setUsersConfig.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 19/04/2022 18:09

# Import needed packages


# Import personal packages
from backend.App.Database import connectDatabase
from backend.App.Database.SetFunctions.setUsersConfig import setUsersConfig
from backend.App.Database.GetFunctions.getUsersConfig import getUsersConfig


def test_set_users_config():
    """
    Test the setUsersConfig function
    """
    # Connect to the database
    db, cursor = connectDatabase()

    # Set the test data
    userName = "Test"
    data = {
        "volume": 0.5,
        "maxTries": 7,
        "wordLength": 6
    }

    setUsersConfig(userName, data)

    config = getUsersConfig(userName)
    assert config[2] == 0.5
    assert config[1] == 7
    assert config[0] == 6
