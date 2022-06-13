from .. import connectDatabase


def getUserName(id):
    db, cursor = connectDatabase()
    cursor.execute("SELECT username FROM Users WHERE id =?", (id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result[0][0]
