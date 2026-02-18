from constants import WORD_LIST
from figure import Figure
from mysterysong import MysterySong
import random
from typing import Self

class GameLoop():
    def __init__(self) -> Self:
        self.__revealed_letters = []
        self.__incorrect_guesses = 0
        self.run_game_loop()
        
    def is_user_word_guess_correct(self, user_input: str, mystery_song: MysterySong) -> bool:
        if (user_input.lower() == mystery_song.get_mystery_song().lower()):
            return True
        return False
    
    def is_user_letter_guess_correct(self, user_input: str, mystery_song: MysterySong) -> bool:
        Found = False
        position = 0
        mystery_song_letters = list(mystery_song.get_mystery_song().lower())
        
        for myster_letter in mystery_song_letters:
            if (user_input.lower() == myster_letter):
                mystery_song.unmask_letter(user_input, position, mystery_song.get_masked_mystery_song())
                Found = True

            position += 1
            
        return Found
        
    def is_mystery_song_unmasked(self, mystery_song: MysterySong) -> bool:
        if (mystery_song.get_mystery_song().lower() == mystery_song.get_masked_mystery_song().lower()):
            return True
        return False
    
    def set_revealed_letters(self, letter: str) -> Self:
        self.__revealed_letters.append(letter) 
    
    def get_revealed_letters(self) -> list:
        return sorted(self.__revealed_letters)

    def set_incorrect_guesses(self) -> Self:
        self.__incorrect_guesses += 1
        
    def get_incorrect_guesses(self) -> int:
        return self.__incorrect_guesses
    
    def set_hangman(self, figure: Figure, incorrect_guesses: int) -> None:
        if (incorrect_guesses == 1):
            figure.add_head()
        if (incorrect_guesses == 2):
            figure.add_body()
        if (incorrect_guesses == 3):
            figure.add_left_arm()
        if (incorrect_guesses == 4):
            figure.add_right_arm()
        if (incorrect_guesses == 5):
            figure.add_left_leg()
        if (incorrect_guesses == 6):
            figure.add_right_leg()
        
    def run_game_loop(self) -> Self:
        running = True
        solved = False
        figure = Figure()
        mystery_song = MysterySong(WORD_LIST[random.randint(0, 199)])
        
        while running:
            print(f"The Mystery Song contains {len(mystery_song.get_mystery_song().replace(" ", ""))} Letters: {mystery_song.get_masked_mystery_song()}")
            print()
            print("Your Letter Guesses So Far Have Been:", self.get_revealed_letters())
            
            while True:
                user_input = str(input("Please Guess A Letter Or Try To Guess The Mystery Song: "))
                user_input = user_input.strip()
                
                if user_input.upper() in self.get_revealed_letters():
                    print(f"You've already guessed '{user_input}'. Try a different letter.")
                    continue
                else:
                    break
    
            
            if (user_input.isalnum() and len(user_input) == 1):
                is_correct = self.is_user_letter_guess_correct(user_input, mystery_song)
                if(is_correct):
                    print(f"Your Guess '{user_input.upper()}' Was Correct!")
                    solved = self.is_mystery_song_unmasked(mystery_song)
                    self.set_revealed_letters(user_input.upper())
                else:
                    print(f"Your Guess '{user_input.upper()}' Was Incorrect!")
                    self.set_incorrect_guesses()
                    self.set_hangman(figure, self.get_incorrect_guesses())
            elif (len(user_input) > 1):
                solved = self.is_user_word_guess_correct(user_input, mystery_song)
                if(solved):
                    print(f"Your Guess '{user_input}' Was Correct!")
                else:
                    print(f"Your Guess '{user_input}' Was Incorrect!")
                    self.set_incorrect_guesses()
                    self.set_hangman(figure, self.get_incorrect_guesses())
                    
            figure.display()
                    
            if(solved):
                print("WELL DONE - You Beat The Hangman!")
                print(f"The Mystery Word was: {mystery_song.get_mystery_song()}")
                running = False
            elif(self.get_incorrect_guesses() == 6):
                print("GAME OVER - The Hangman Got You!")
                print(f"The Mystery Word was: {mystery_song.get_mystery_song()}")
                running = False
                
            