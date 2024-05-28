from dotenv import load_dotenv
from flask import Flask, render_template, request,redirect
from spotify_youtube.spotify_playlist_scrapper import SpotifyPlaylistScrapper
from spotify_youtube.youtube_playlist_tool import YoutubeTool
from spotify_youtube.database_manager import DatabaseManager

load_dotenv()

app = Flask(__name__)

db_manager = DatabaseManager()
spotify_playlist = SpotifyPlaylistScrapper(db_manager)
youtube_tool = YoutubeTool(db_manager, spotify_playlist)


@app.route('/', methods=['GET', 'POST'])
def index():
    not_found_songs = None

    if request.method == 'POST':

        if request.form['playlist_url'] == "python odyssey":
            return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        spotify_playlist.set_playlist_url(request.form['playlist_url'])
        spotify_playlist.scrap_playlist()
        privacy_status = request.form['privacy_status']
        playlist_id, not_found_songs = youtube_tool.create_playlist_and_fill(spotify_playlist.get_playlist_title(), privacy_status)
        return render_template('result.html', playlist_id=playlist_id, not_found_songs=not_found_songs)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
