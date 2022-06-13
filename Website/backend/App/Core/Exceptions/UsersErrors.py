#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : UsersErrors.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/4

# Import needed packages


# Import personal packages


class UserNotFound(Exception):
    def __init__(self):
        self.status = "UserNotFound"


class UsernameAlreadyUsed(Exception):
    def __init__(self):
        self.status = "UsernameAlreadyUsed"
