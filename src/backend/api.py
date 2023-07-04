import sqlite3

class API():
    def __init__(self):
        self.cursor, self.connection = self.connect()
      
    # Generic connect and close methods
    def connect(self):
        connection = sqlite3.connect('./mario.db')
        cursor = connection.cursor()
        return cursor, connection

    def close(self, connection):
        # Save the changes
        connection.commit()
        connection.close()

    def get_all_character_names(self):
        self.cursor.execute('SELECT name, type FROM Character;')
        results = self.cursor.fetchall()
        return results