from random import randint
from constants.constants_memory_game import LOWER_RANGE, UPPER_RANGE, WAITING_TIME
from time import sleep
import pyinputplus as pyip


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        list_size = self.difficulty
        sequence_list = [] * list_size
        for item in range(list_size):
            sequence_list.append(randint(LOWER_RANGE, UPPER_RANGE))
        return sequence_list

    def get_list_from_user(self):
        list_size = self.difficulty
        user_list = [] * list_size
        for item in range(list_size):
            user_list.append(pyip.inputInt(
                """\rPlease enter the numbers you remember.
                \rReminder! the number should be between {} to {} and the amount is {}: """
                .format(LOWER_RANGE, UPPER_RANGE, list_size), min=LOWER_RANGE, lessThan=UPPER_RANGE + 1
            ))
        return user_list

    def is_list_equal(self, generated_list, user_list):
        return generated_list == user_list

    def play(self):
        generated_list = self.generate_sequence()
        print(generated_list, end="")
        sleep(WAITING_TIME)
        user_list = self.get_list_from_user()
        result = self.is_list_equal(generated_list, user_list)
        return result
