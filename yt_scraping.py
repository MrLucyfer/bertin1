import requests
from bs4 import BeautifulSoup as bs


def search(title):
    query = title
    url = 'https://www.youtube.com/results?search_query=' + query

    result = requests.get(url)

    soup = bs(result.content, 'html.parser')

    a = soup.find('a',attrs={'class':'yt-uix-tile-link'})
    return a['href'].split('=')[1]