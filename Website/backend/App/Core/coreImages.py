# Import needed packages
import string
import random
import os
from PIL import Image


# Import personal packages
from ..Database import connectDatabase
from ..Database.GetFunctions.getUsersId import getUsersId


def generate_unique_filename(length: int, fileExtension: str) -> str:
    query = '''SELECT * FROM Users WHERE picture=?;'''

    alphabet = string.ascii_letters + string.digits
    code = ''.join(random.choice(alphabet) for i in range(length))

    arg = (code + '.' + fileExtension,)

    db, cursor = connectDatabase()
    cursor.execute(query, arg)
    data = cursor.fetchall()
    db.close()

    if len(data) == 0:
        return code
    else:
        return generate_unique_filename(length, fileExtension)


def save_candidate_picture(username: str, picturePath: str, file) -> None:
    fileExtension = file.format.lower()

    uniqueCode = generate_unique_filename(6, fileExtension)
    uniqueCode += "." + fileExtension

    file.save(picturePath + uniqueCode)

    userId = getUsersId(username)

    removeQuery = '''SELECT picture FROM Users WHERE id=?;'''
    removeArg = (userId,)

    addQuery = "UPDATE Users SET picture=? WHERE id=?;"
    addArgs = (uniqueCode, userId)

    db, cursor = connectDatabase()
    cursor.execute(removeQuery, removeArg)
    data = cursor.fetchall()

    if data[0][0] is not None:
        os.remove(os.path.join(picturePath, data[0][0]))

    cursor.execute(addQuery, addArgs)
    db.commit()
    db.close()


def readImage(username: str, picturePath: str):
    db, cursor = connectDatabase()
    cursor.execute('''SELECT picture FROM Users WHERE username=?;''', (username,))
    data = cursor.fetchall()
    db.close()
    return Image.open(picturePath + data[0][0])
