from constants import WORD_LIST
from figure import Figure
from mysterysong import MysterySong


def main():
    figure = Figure()
    figure.add_head()
    figure.add_body()
    figure.add_left_arm()
    figure.add_right_arm()
    figure.add_left_leg()
    figure.add_right_leg()
    
    mystery_song = MysterySong("'39")
    print(mystery_song.get_mystery_song())
    mystery_song.set_mystery_song("Bohemian Rhapsody")
    print(mystery_song.get_mystery_song())

if __name__ == "__main__":
    main()