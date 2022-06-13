#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : coreScore.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 28/04/2022 19:05

# Import needed packages


# Import personal packages
from App.Database.AddFunctions.addLeaderboard import addScore


def rateGame(nbLetter: int, nbTries: int, maxTries: int) -> int:
    """
    Function to rate the game
    :param nbLetter: the number of letter in the word
    :param nbTries: the number of tries
    :param maxTries: the maximum number of tries
    :return: the score of the game
    """
    rate = int(nbLetter * (maxTries - nbTries) / maxTries)
    return rate


def scoreGame(nbLetter: int, nbTries: int, maxTries: int, userId: int) -> None:
    """
    Function to score the game
    :param nbLetter: the number of letter in the word
    :param nbTries: the number of tries
    :param maxTries: the maximum number of tries
    :param userId: the user's id
    :return: True if the score has been added
    """
    score = rateGame(nbLetter, nbTries, maxTries)
    addScore(score, userId)
