import random
import Live
from currency_converter import CurrencyConverter
from Score import add_score


def get_money_interval(diff):
    interval = 5 - int(diff)
    return interval


def get_guess_from_user(amount):
    guess = Live.valid_num(1, 1000, input(f"enter how much you think the {amount} of USD in ILS is: "))
    return guess


def play(diff):
    amount = random.randrange(1, 100)
    total = round(CurrencyConverter().convert(amount, 'USD', 'ILS'), 2)
    interval = get_money_interval(diff)
    minimum = total - interval
    maximum = total + interval
    guess = get_guess_from_user(amount)
    print(total)
    if minimum <= float(guess) <= maximum:
        add_score(diff)

    else:
        print("you lost")
        return False

# play(5)













