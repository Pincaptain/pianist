import time

from selenium import webdriver
from pynput.keyboard import Controller

from entities.song import Song


class PlaySong:
    def __init__(self, song: Song):
        self.browser = webdriver.Chrome()
        self.song = song
        self.keyboard = Controller()

        self.browser.get('https://virtualpiano.net/')
        self.browser.execute_script('window.focus();')

        self.keyboard.type(self.song.strokes, )
