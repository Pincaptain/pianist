from use_cases.play_song import PlaySong
from repositories.song_repository import SongRepository

if __name__ == '__main__':
    PlaySong(SongRepository().get_song('Naruto'))
