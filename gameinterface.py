from constants import WORD_LIST
from figure import Figure
from mysterysong import MysterySong
import random

class GameInterface():
    def __init__(self):
        self.run_game_loop()
        
    def run_game_loop(self):
        running = True
        
        figure = Figure()
        mystery_song = MysterySong(WORD_LIST[random.randint(0, 199)])
        print(mystery_song.get_mystery_song())
        
        while running:
            
            figure.add_head()
            figure.add_body()
            figure.add_left_arm()
            figure.add_right_arm()
            figure.add_left_leg()
            figure.add_right_leg()

            running = False