# import logging
from Live import load_game, welcome
from flask_app import app
from Utils import screen_cleaner

# Main program that gets username as an input and perform input validation.
# The only input allowed is alpha characters without spaces.


def entry_point():
    loaded_game = load_game()
    return loaded_game


def game_result(result):
    if result:
        return "Congratulations you won the game!"
    else:
        return """Sorry... you lost!
               \rBetter luck next time... :)"""


def main():  # ************************ To adjacent docstring to relevant info + add return value/s ****************** #
    # """Takes in a person name (string) - name, returns a message (string) with name inside"""
    # """
    #     Returns both the chosen game number and difficulty level.
    #
    #             Inputs:
    #                     game_number (int): An input from the user of the game number chosen.
    #                     difficulty (int): An input from the user of difficulty as a number.
    #
    #             Returns:
    #                     game_number and difficulty (int): integers chosen by the user.
    #     """
    control_var = True
    while control_var:
        try:
            user_name = input("Please Enter your name: ")
            control_var = user_name.isalpha()
            if not control_var:
                control_var = True
                raise ValueError
            user_name = user_name.capitalize()
            print(welcome(user_name))
            break
        except ValueError:
            print("Username can only contain alpha characters and without spaces.")


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(name)s:%(funcName)s:%(lineno)d:%(levelname)s] %(message)s")
    main()
    load_game = entry_point()
    game_result_msg = game_result(load_game[2])
    print(game_result_msg)
    screen_cleaner()
    app.run(host="0.0.0.0", port=5000, debug=False)
