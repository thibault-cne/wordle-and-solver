#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : ReplaysError.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/16

# Import needed packages


# Import personal packages

class GameIDNotFoundError(Exception):
    """
    Raised when a game ID is not found in the database
    """
    pass


class NoPlayingGameError(Exception):
    """
    Raised when a player is not playing a game
    """
    pass


class GameHasEndedError(Exception):
    """
    Raised when a game has already ended
    """
    pass
