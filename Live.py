import pyinputplus as pyip
from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from Score import Score

# from GuessGame import play as guess_game_play
# from MemoryGame import play as memory_game_play
# from CurrencyRouletteGame import play as currency_roulette_game_play


def welcome(name):
    """Takes in a person name (string) - name, returns a message (string) with name inside"""
    message = ("\nHello {} and welcome to the World of Games (WoG).\n"
               "Here you can find many cool games to play.\n").format(name)
    return message


# Choosing a game
def load_game():
    """
    Returns both the chosen game number and difficulty level.

            Inputs:
                    game_number (int): An input from the user of the game number chosen.
                    difficulty (int): An input from the user of difficulty as a number.

            Returns:
                    game_number and difficulty (int): integers chosen by the user.
    """
    print("Please choose a game to play: ")
    message = ("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
               "2. Guess Game - guess a number and see if you chose like the computer.\n"
               "3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n"
               )
    print(message)
    game_number = pyip.inputInt(min=1, lessThan=4)
    difficulty = pyip.inputInt("Please choose game difficulty from 1 to 5: ", min=1, lessThan=6)
    if game_number == 1:
        game_result = MemoryGame(difficulty).play()
        # game_result = memory_game_play(difficulty)
    elif game_number == 2:
        game_result = GuessGame(difficulty).play()
        # game_result = guess_game_play(difficulty)
    else:
        game_result = CurrencyRouletteGame(difficulty).play()
        # game_result = currency_roulette_game_play(difficulty)
    if game_result:
        Score(difficulty).add_score()
    return game_number, difficulty, game_result
