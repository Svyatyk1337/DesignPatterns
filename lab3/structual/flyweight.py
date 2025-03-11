class Character:
    def __init__(self, char):
        self.char = char

    def display(self, x, y):
        return f"Character '{self.char}' displayed at ({x}, {y})"

class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(char):
        if char not in CharacterFactory._characters:
            CharacterFactory._characters[char] = Character(char)
        return CharacterFactory._characters[char]