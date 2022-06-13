#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : retrieveCypherWord.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 21/04/2022 17:17

# Import needed packages
from werkzeug.security import check_password_hash


# Import personal packages
from .coreFiles import open_txt
from .Exceptions.WordsExceptions import NoWordFound


def retrieveCypherWord(cypherWord: str) -> str:
    """
    Retrieve the word from the cypher word

    :param cypherWord: The cypher word
    :return: The cypher word
    """
    data = open_txt("l_5")

    for word in data:
        word = word[:-1]
        if check_password_hash(cypherWord, word):
            return word

    raise NoWordFound("No word found")
