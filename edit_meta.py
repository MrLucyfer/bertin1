import spotify_api as sp
import os

playlist_id = '7wgwcYspJRXjprqOfFMJzL'
token = sp.refresh_token()
titles = sp.getTitles(playlist_id, token)

def editMeta(title):
    command = f'id3v2 -t "{title[0]}" -a "{title[1]}" -A "{title[2]}" ../new_songs/"{title[0]}".mp3'
    print(command)
    os.system(command)