from os import name, system
from time import sleep

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 500


def screen_cleaner():
    # for mac and linux
    if name == "posix":
        system("clear")
    # for windows platform
    else:
        system("cls")
