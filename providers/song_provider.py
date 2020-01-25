import requests
from bs4 import BeautifulSoup

from entities.song import Song


class SongProvider:
    def __init__(self):
        self.base_url = 'https://virtualpiano.net/?s='

    def provide_song(self, title: str):
        prepared_title = title.replace(' ', '+')
        prepared_url = f'{self.base_url}{prepared_title}'

        response = requests.get(prepared_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        div = soup.find('div', {'class': 'entry-content'})
        div.find('pre').extract()

        song_title = soup.find('h1', {'class': 'entry-title'}).getText()
        song_strokes = str(div.getText()).strip().replace(' ', '').replace('\n', '')
        song = Song(song_title, song_strokes)

        return song
