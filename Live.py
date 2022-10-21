def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


def load_game():
    game_choose = input("""please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you choose like the computers
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
""")
    return valid_num(1, 3, game_choose)


def valid_num(minimum, maximum, number):
    while True:
        if type(number) != "int":
            if number.isdigit():
                if minimum <= int(number) <= maximum:
                    return number
                else:
                    number = input(f"you must choose number between {minimum} - {maximum}: ")
            else:
                number = input(f"please enter numbers only between {minimum} - {maximum}: ")


def difficulty():
    diff = input("please choose game difficulty between 1 - 5: ")
    return valid_num(1, 5, diff)

