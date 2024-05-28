import sqlite3

class DatabaseManager:
    def __init__(self):
        self.db_name = ":memory:"  # You can modify this to use a file-based database
        self._connection = None

    def get_connection(self):
        if self._connection is None:
            self.connect()
        return self._connection

    def connect(self):
        try:
            self._connection = sqlite3.connect(self.db_name)
            print("Connection successfully established")
        except sqlite3.Error as e:
            print(f"Error while connecting to the database: {e}")

    def disconnect(self):
        if self._connection:
            self._connection.close()
            self._connection = None
            print("Disconnected from the database")

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
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
            connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Error while creating table: {e}")

    def insert_song(self, song_artist, song_name, album_name="no album"):
        self.create_table()
        insert_into_table = '''
        INSERT INTO SONGS (song_artist, song_name, album_name) 
        VALUES (?, ?, ?)'''
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute(insert_into_table, (song_artist, song_name, album_name))
            connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Error inserting song into the database: {e}")

    def get_all_songs(self):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT song_artist, song_name, album_name FROM SONGS")
            songs = cursor.fetchall()
            cursor.close()
            return songs
        except sqlite3.Error as e:
            print(f"Error while retrieving data from database: {e}")
