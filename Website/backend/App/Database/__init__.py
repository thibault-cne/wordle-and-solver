#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : __init__.py
#  Description : File to generate the database
#
#  --
#
#  Last modification : 2022/3/31

# Import needed packages
from typing import Tuple
import os


# Import personal packages
from sqlite3 import Connection, Cursor, connect


def connectDatabase() -> Tuple[Connection, Cursor]:
    """
    Function to return the connection object to the database and a cursor object

    :return: return a tuple of the database object and a cursor object
    """
    path = os.path.dirname(os.path.abspath(__file__))
    dbPath = os.path.join(path, 'database.db')

    db = connect(dbPath)
    cursor = db.cursor()
    return db, cursor


def create_database() -> str:
    """
    Functions to generate the query to create the database

    :return: a string to create th database
    """
    # Script for the database
    query = '''
        DROP TABLE IF EXISTS Users;
        DROP TABLE IF EXISTS Achievements;
        DROP TABLE IF EXISTS Users_achievements;
        DROP TABLE IF EXISTS Replays;
        DROP TABLE IF EXISTS Config;
        DROP TABLE IF EXISTS Users_stats;
        DROP TABLE IF EXISTS Leaderboard;
        DROP TABLE IF EXISTS PartieTI;

        CREATE TABLE Users
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            picture TEXT,
            password TEXT NOT NULL
        );

        CREATE TABLE Achievements
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        );
        
        CREATE TABLE Users_achievements
        (
            id INTEGER PRIMARY KEY,
            achievements INT NOT NULL,
            FOREIGN KEY (id) REFERENCES Achievements(id)
        );

        CREATE TABLE Replays
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            replay TEXT NOT NULL,
            playingState TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            neededWord TEXT NOT NULL,
            answerLength INTEGER,
            gameMode TEXT NOT NULL,
            maxTries INTEGER NOT NULL DEFAULT 6,
            FOREIGN KEY (user_id) REFERENCES Users(id)
        );

        CREATE TABLE Config
        (
            id INTEGER PRIMARY KEY,
            wordlength INT NOT NULL,
            maxTries INT NOT NULL,
            FOREIGN KEY (id) REFERENCES Users(id)
        );

        CREATE TABLE Users_stats
        (
            id INTEGER PRIMARY KEY,
            FOREIGN KEY (id) REFERENCES Users(id)
        );

        CREATE TABLE Leaderboard
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            score INTEGER NOT NULL,
            FOREIGN KEY (id) REFERENCES Users(id)
        );
        
        CREATE TABLE PartieTI
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            userId INT NOT NULL,
            replay TEXT NOT NULL,
            playingState TEXT NOT NULL,
            liste_reponse TEXT,
            FOREIGN KEY (id) REFERENCES Users(id)
        );
        '''

    return query


if __name__ == "__main__":
    """query = create_database()

    db = connect('database.db')
    cursor = db.cursor()
    cursor.executescript(query)     # Create database
    db.commit()
    cursor.close()
    db.close()"""


    query = """"""      # Insert query here
    db, cursor = connectDatabase()
    cursor.execute(query)
    db.commit()
    db.close()
