from .. import connectDatabase


def getLeaderBoard():
    db, cursor = connectDatabase()
    cursor.execute("SELECT * FROM Leaderboard ORDER BY score DESC")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
