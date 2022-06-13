#   Copyright (c)
#   Project : project2-E19
#  #
#   --
#  #
#   Author : thibault
#   File : dailyWordCore.py
#   Description : *Enter description here*
#  #
#   --
#  #
#   Last modification : 25/04/2022 16:27

# Import needed packages
from random import shuffle
from datetime import datetime


# Import personal packages
from App.Database import connectDatabase
from .coreFiles import open_txt, write_file


def setAllWord() -> None:
    """
    Set all words and current date in the file dailyWord.txt
    """
    data = open_txt("dictionnary")
    shuffle(data)
    today = datetime.today().strftime("%d-%m-%Y")
    data[0] = today + "\n"
    write_file("dailyWord", "txt", "Text", data)


def updateWords() -> None:
    data = open_txt("dailyWord")
    today = datetime.today().strftime("%d-%m-%Y")
    data[1] = today + "\n"
    write_file("dailyWord", "txt", "Text", data[1:])


def getDailyWord() -> str:
    """
    Get the daily word from the file dailyWord.txt
    """
    data = open_txt("dailyWord")
    today = datetime.today().strftime("%d-%m-%Y")
    if data[0][:-1] != today:
        updateWords()
        endAllOldGames()
        return getDailyWord()
    else:
        return data[1][:-1]


def endAllOldGames() -> None:
    """
    End all old games
    """
    query = """UPDATE Replays SET playingState = 'ended'
    WHERE playingState = 'playing';"""

    db, cursor = connectDatabase()
    cursor.execute(query)
    db.commit()
    db.close()


if __name__ == "__main__":
    setAllWord()
