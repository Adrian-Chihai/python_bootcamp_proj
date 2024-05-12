import sqlite3
class DatabaseManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_table(self):
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS
        SONGS (
        'song_id' INTEGER PRIMARY KEY AUTOINCREMENT,
        'song_artist' CHAR(50),
        'song_name' CHAR(100),
        'album_name' CHAR(100)
        )'''

        try:
            cursor = self.db_connection.cursor()
            cursor.execute(create_table_sql)
            self.db_connection.commit()
        except sqlite3.Error as e:
            print(f"Error while creating table: {e}")

    def insert_song(self, song_artist, song_name, album_name="no album"):
        self.create_table()
        insert_into_table = '''
        INSERT INTO SONGS (song_artist, song_name, album_name) 
        VALUES (?, ?, ?)'''
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(insert_into_table, (song_artist, song_name, album_name))
            self.db_connection.commit()
            print("Song inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting song into the database: {e}")

    def get_all_songs(self):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT * FROM SONGS")
            self.db_connection.commit()
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error while retrieving data from database: {e}")





