from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import time

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


class YoutubeTool:

    def __init__(self, db_manager, spotify_playlist):
        self.db_manager = db_manager
        self.spotify_playlist = spotify_playlist

    def get_authenticated_service(self):
        flow = InstalledAppFlow.from_client_secrets_file("spotify_youtube\\client_secret.json", SCOPES)
        credentials = flow.run_local_server(port=0)
        return build('youtube', 'v3', credentials=credentials)

    def create_playlist(self, youtube, playlist_name, privacy_status):
        request = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": playlist_name,
                },
                "status": {
                    "privacyStatus": privacy_status
                }
            }
        )
        response = request.execute()
        return response

    def search_youtube(self, youtube, query):
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=1
        )
        response = request.execute()
        if response['items']:
            return response['items'][0]['id']['videoId']
        return None

    def add_video_to_playlist(self, youtube, playlist_id, video_id, max_retries=3):
        for attempt in range(max_retries):
            try:
                request = youtube.playlistItems().insert(
                    part="snippet",
                    body={
                        "snippet": {
                            "playlistId": playlist_id,
                            "resourceId": {
                                "kind": "youtube#video",
                                "videoId": video_id
                            }
                        }
                    }
                )
                response = request.execute()
                return response
            except HttpError as e:
                print(f"An HTTP error {e.resp.status} occurred: {e.content}")
                if e.resp.status in [500, 503]:
                    print(f"Retrying... ({attempt + 1}/{max_retries})")
                    time.sleep(2 ** attempt)
                else:
                    raise
        raise Exception(f"Failed to add video ID {video_id} to playlist ID {playlist_id} after {max_retries} attempts")

    def create_playlist_and_fill(self, playlist_name, privacy_status):
        youtube = self.get_authenticated_service()
        playlist_response = self.create_playlist(youtube, playlist_name, privacy_status)
        playlist_id = playlist_response['id']
        print(f"Playlist ID: {playlist_id}")

        songs = self.db_manager.get_all_songs()
        print("Songs to be added:", songs)

        not_found_songs = []

        for song in songs:
            if len(song) != 3:
                print(f"Unexpected song format: {song}")
                continue
            artist, title, album = song
            query = f"{artist} {title} {album}"
            video_id = self.search_youtube(youtube, query)
            if video_id:
                try:
                    self.add_video_to_playlist(youtube, playlist_id, video_id)
                    print(
                        f"Added video ID {video_id} for '{title}' by '{artist}' from album '{album}' to playlist ID {playlist_id}")
                except Exception as e:
                    print(f"Failed to add video ID {video_id} for '{title}' by '{artist}' from album '{album}': {e}")
                    not_found_songs.append(f"{title} by {artist} from album {album}")
            else:
                print(f"Could not find a video for '{title}' by '{artist}' from album '{album}'")
                not_found_songs.append(f"{title} by {artist} from album {album}")

        return playlist_id, not_found_songs