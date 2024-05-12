from database_manager import DatabaseManager
from playlist_scrapper import PlaylistScrapper
from sqlite_connection import SQLiteConnection

sqlite_connection = SQLiteConnection()
database_manager = DatabaseManager(sqlite_connection.connection)
playlist_collector = PlaylistScrapper(database_manager)

playlist_collector.scrap_playlist()

for song in database_manager.get_all_songs():
    print(song)

sqlite_connection.disconnect()

database_manager = DatabaseManager(sqlite_connection.connection)
database_manager.get_all_songs()
