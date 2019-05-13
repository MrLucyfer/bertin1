import os
import yt_scraping as yt
import spotify_api as sp
import edit_meta as meta

def editString(str):
    return str.replace(' ', '\ ')

def run(id):
    token = sp.refresh_token()
    titles = sp.getTitles(id, token)
    for title in titles:
        try:
            print ('Song: ' + title[0])
            def_title = editString(title[0])
            vid_id = yt.search(title[0] + 'lyrics')
            command = './script.sh ' + def_title + ' ' + 'https://www.youtube.com/watch?v=' +  vid_id
            print(command)
            os.system(command)
            meta.editMeta(title)
        except:
            print("Video not found!")    


