import os
import yt_scraping as yt
import spotify_api as sp



def editString(str):
    return str.replace(' ', '\ ')

def run(id):
    token = sp.refresh_token()
    titles = sp.getTitles(id, token)
    for title in titles:
        try:
            print ('Song: ' + title)
            def_title = editString(title)
            vid_id = yt.search(title + 'lyrics')
            command = './script.sh ' + def_title + ' ' + 'https://www.youtube.com/watch?v=' +  vid_id
            print(command)
            os.system(command)
        except:
            print("Video not found!")    
