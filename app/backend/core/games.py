from fastapi import HTTPException
from random_word import RandomWords

from app.backend.schema.general import Game


def generate_new_word(word: str, game: Game):
    if game.last_word != "":  # Check if it's the first round
        word = word.lower()
        last_letter = list(game.last_word)[-1]
        if list(word)[0] != last_letter:
            raise HTTPException(status_code=400, detail="Not a possible word")
    random = RandomWords()
    found = False
    while not found:
        random_word = random.get_random_word().lower()
        if list(random_word)[0] == list(word)[-1]:
            print(word)
            found = True
    return random_word


def calculate_score():
    pass
