import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

set SPOTIPY_CLIENT_ID= e53291ba5a474c7e852304474c92e1d8
set SPOTIPY_CLIENT_SECRET= 6a6bc9c277d94480b46f47c37fec0493
set SPOTIPY_REDIRECT_URI= http://example.com

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])
