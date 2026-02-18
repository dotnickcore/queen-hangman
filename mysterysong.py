from typing import Self


class MysterySong:
    def __init__(self, mystery_song: str) -> Self:
        self.__mystery_song = mystery_song
        self.__masked_mystery_song = self.mask_mystery_song(mystery_song)
        
    def get_mystery_song(self) -> str:
        return self.__mystery_song
    
    def set_mystery_song(self, mystery_song: str) -> Self:
        self.__mystery_song = mystery_song
        self.__masked_mystery_song = self.mask_mystery_song(mystery_song)
    
    def get_masked_mystery_song(self) -> str:
        return self.__masked_mystery_song
    
    def mask_mystery_song(self, song: str) -> str:
        result_list = []
        for char in song:
            if char.isalnum():
                result_list.append('_')
            else:
                result_list.append(char)
        return "".join(result_list)
    
    def unmask_letter(self, mystery_letter: str, position: int, masked_song: str) -> Self:
        letter_list = list(masked_song)
        letter_list[position] = mystery_letter
        
        self.__masked_mystery_song = "".join(letter_list)
        