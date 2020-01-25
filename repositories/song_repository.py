from providers.song_provider import SongProvider


class SongRepository:
    def __init__(self):
        self.song_provider = SongProvider()

    def get_song(self, title):
        return self.song_provider.provide_song(title)
