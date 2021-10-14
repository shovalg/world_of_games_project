from constants.constants_currency_roulette_game import API_KEY, RESULT, ILS, LOWER_RANGE, UPPER_RANGE
from random import randint
import pyinputplus as pyip
import requests


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_current_ils2shekel_rate(self):
        response = requests.get("https://api.fastforex.io/fetch-one?from=USD&to=ILS&api_key={}".format(API_KEY))
        ils2shekel_rate = response.json()[RESULT][ILS]
        return ils2shekel_rate

    def rand_amount_of_coins(self):
        amount = randint(LOWER_RANGE, UPPER_RANGE)
        return amount

    def get_money_interval(self, ils2shekel_rate, usd_amount, difficulty):
        total_amount = ils2shekel_rate * usd_amount
        money_min_interval = total_amount-(5-difficulty)
        money_max_interval = total_amount+(5-difficulty)
        return money_min_interval, money_max_interval

    def get_guess_from_user(self, usd_amount):
        user_guess = pyip.inputFloat(
            "Please try to estimate the current value of {} USD in ILS: "
            .format(usd_amount), min=0
        )
        return user_guess

    def is_guess_correct(self, min_interval, max_interval, user_guess):
        return min_interval <= user_guess <= max_interval

    def play(self):
        ils2shekel_rate = self.get_current_ils2shekel_rate()
        usd_amount = self.rand_amount_of_coins()
        min_interval, max_interval = self.get_money_interval(ils2shekel_rate, usd_amount, self.difficulty)
        user_guess = self.get_guess_from_user(usd_amount)
        result = self.is_guess_correct(min_interval, max_interval, user_guess)
        return result
