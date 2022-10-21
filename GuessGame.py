from random import randrange


def generate_number(diff):
    secret_number = randrange(1, int(diff) + 1)
    return secret_number


def get_guess_from_user(diff):
    guess = input(f"guess a number between 1 to {int(diff)+1}: ")
    return guess


def compare_results(diff):
    if int(generate_number(diff)) == int(get_guess_from_user(diff)):
        return True
    else:
        return False


def play(diff):
    if compare_results(diff):
        print("you won")
    else:
        print("you lost")

