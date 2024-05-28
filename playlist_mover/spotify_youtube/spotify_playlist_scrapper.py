import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import re

class SpotifyPlaylistScrapper:
    def __init__(self, db_manager):
        self.__playlist_url = None
        self.__client_credentials_manager = SpotifyClientCredentials(
            os.getenv("SPOTIFY_CLIENT_ID"), os.getenv("SPOTIFY_CLIENT_SECRET")
        )
        self.__sp = spotipy.Spotify(client_credentials_manager=self.__client_credentials_manager)
        self.__db_manager = db_manager

    def set_playlist_url(self, url):
        if not re.match(r'^(https://open\.spotify\.com/playlist/|spotify:playlist:)[a-zA-Z0-9]+$', url):
            raise ValueError("Invalid Spotify playlist URL format. URL must start with 'https://open.spotify.com/playlist/' or 'spotify:playlist:' and be followed by a playlist ID.")
        self.__playlist_url = url
        print(f"Playlist URL set to: {self.__playlist_url}")

    def scrap_playlist(self):
        print(self.get_playlist_title())
        self.__get_playlist_songs()

    def get_playlist_title(self):
        return self.__sp.playlist(self.__playlist_url)['name']

    def __get_playlist_songs(self):
        playlist_data = self.__sp.playlist_items(self.__playlist_url)
        while True:
            for song in playlist_data['items']:
                track = song['track']
                if track is not None:
                    artist = track['artists'][0]['name']
                    song_name = track['name']
                    album_name = track['album']['name']
                    self.__db_manager.insert_song(artist, song_name, album_name)
                    print(f"{artist} - {song_name}")
            if playlist_data['next']:
                playlist_data = self.__sp.next(playlist_data)
            else:
                break
