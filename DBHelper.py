import sqlite3


class DBHelper:
    def __init__(self):
        self.db = sqlite3.connect('Classes.db')
        self.cursor = self.db.cursor()

    def getAll(self):
        return self.cursor.execute("SELECT * FROM [Классы]").fetchall()

    def updateItem(self, answer1,  answer2, answer3, answer4, answer5,
                   answer6, answer7, answer8, answer9, answer10, className):
        self.cursor.execute("""UPDATE [Классы] SET [1 score] = ?, [2 score] = ?, [3 score] = ?, [4 score] = ?, 
                [5 score] = ?, [6 score] = ?, [7 score] = ?, [8 score] = ?, [9 score] = ?, [10 score] = ? WHERE Class = ?""",
                       (answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10,
                        className))
        self.db.commit()

    def addItem(self, className, answer1, answer2, answer3, answer4, answer5,
                  answer6, answer7, answer8, answer9, answer10):
        values = (className, answer1, answer2, answer3, answer4, answer5,
                  answer6, answer7, answer8, answer9, answer10)
        sqlite_insert_query = """INSERT INTO [Классы]
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        self.cursor.execute(sqlite_insert_query, values)
        self.db.commit()

    def deleteItem(self, className):
        self.cursor.execute("""DELETE FROM [Классы] WHERE Class = ?""", (className,))
        self.db.commit()

    def close(self):
        self.db.close()
