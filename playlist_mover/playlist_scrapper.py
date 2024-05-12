import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials

class PlaylistScrapper:
    def __init__(self, db_manager):
        self.__client_credentials_manager = SpotifyClientCredentials(os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET"))
        self.__sp = spotipy.Spotify(client_credentials_manager=self.__client_credentials_manager)
        self.__db_manager = db_manager

    def scrap_playlist(self):
        playlist_url = input("Enter a playlist URL (playlist needs to be public): ")
        print(self.__get_playlist_title(playlist_url))
        self.__get_playlist_songs(playlist_url)

    def __get_playlist_title(self, playlist_url):
        return self.__sp.playlist(playlist_url)['name']

    def __get_playlist_songs(self, playlist_url):
        playlist_data = self.__sp.playlist_items(playlist_url)
        for song in playlist_data['items']:
            track = song['track']
            artist = track['artists'][0]['name']
            song_name = track['name']
            album_name = track['album']['name']
            # print(f"Song: {artist}:{song_name} - Album: {album_name}")
            self.__db_manager.insert_song(artist, song_name, album_name)

