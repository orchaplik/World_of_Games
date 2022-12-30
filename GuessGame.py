from random import randrange
from Score import add_score


def generate_number(diff):
    secret_number = randrange(1, int(diff) + 1)
    return secret_number


def get_guess_from_user(diff):
    guess = input(f"guess a number between 1 to {int(diff)+1}: ")
    return guess


def compare_results(diff):
    if int(generate_number(diff)) == int(get_guess_from_user(diff)):
        return "You Won!!"
    else:
        return "You Lost!!"


def play(diff):
    if compare_results(diff):
        add_score(diff)
    else:
        print("you lost")

