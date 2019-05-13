import requests
import ast

client_id = '981dc6ad047c4181939c93822c050513'

base_encoded = 'OTgxZGM2YWQwNDdjNDE4MTkzOWM5MzgyMmMwNTA1MTM6ODFjZmRlOWRlMGUwNDBjMjhlYmQyYWNjZTM2NGE3OGQ='

token_url = "https://accounts.spotify.com/api/token"

def refresh_token():
	payload = "grant_type=refresh_token&refresh_token=AQDMhEggFfm06w--YnbavsH3YHhFSG-VSGS-zP1w8T4AR1ja_eBDTXO2TNFpnOqTgXwqRWhc77BmzNPjaeBA4suNScShAmhy8nSDmYLyt8ph2j2MhwHMoVCcMctg96_bM12zxA"	
	headers = {
	'Authorization': "Basic " + base_encoded,
	'Content-Type': "application/x-www-form-urlencoded",
	}

	response = requests.request("POST", token_url, data=payload, headers=headers)
	r = ast.literal_eval(response.text)
	return r["access_token"]

def getTitles(id, token):
    playlist_id = id
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks?fields=items(track(name, album(name, artists)))'
    titles = []
    headers = {"Authorization": "Bearer " + token}
    r = requests.get(url, headers=headers)
    d = ast.literal_eval(r.text)
    for item in (d["items"]):
        titles.append([str(item["track"]["name"]), str(item["track"]["album"]["artists"][0]["name"]), str(item["track"]["album"]["name"])])
    return titles
	
    


