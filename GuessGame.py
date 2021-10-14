from random import randint
from constants.constants_guess_game import LOWER_RANGE
import pyinputplus as pyip


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_number(self):
        secret_number = randint(LOWER_RANGE, self.difficulty)
        return secret_number

    def get_guess_from_user(self):
        guessed_number = pyip.inputInt(
            "Please guess a number between 1 to {}: ".format(self.difficulty), min=LOWER_RANGE, lessThan=self.difficulty+1
        )
        return guessed_number

    def compare_results(self, secret_number, guessed_number):
        return secret_number == guessed_number

    def play(self):
        secret_number = self.generate_number()
        guessed_number = self.get_guess_from_user()
        result = self.compare_results(secret_number, guessed_number)
        return result
