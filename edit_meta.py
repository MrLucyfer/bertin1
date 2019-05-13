import spotify_api as sp
import os

playlist_id = '7wgwcYspJRXjprqOfFMJzL'
token = sp.refresh_token()
titles = sp.getTitles(playlist_id, token)

def editMeta(title):
    for meta in title:
        command = f'id3v2 -t "{meta[0]}" -a "{meta[1]}" -A "{meta[2]}" new_songs/"{meta[0]}".mp3'
        print(command)
        os.system(command)