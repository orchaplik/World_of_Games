from random import randrange
import Live
import time
from Score.Score import add_score
from Score.Utils import screen_cleaner


def generate_sequence(diff):
    list_of_nums = []
    i = 1
    while i <= int(diff):
        list_of_nums.append(int(randrange(1, 101)))
        i = i + 1
    print(list_of_nums)
    time.sleep(0.7)
    screen_cleaner()
    return list_of_nums


def get_list_from_user(diff):
    list_of_nums_user = []
    i = 1
    while i <= int(diff):
        guess_num = Live.valid_num(1, 101, input("Enter Number Between 1-101: "))
        i = i + 1
        list_of_nums_user.append(int(guess_num))
    return list_of_nums_user


def is_list_equal(diff):
    is_equal = generate_sequence(diff) == get_list_from_user(diff)
    return is_equal


def play(diff):
    if is_list_equal(diff):
        add_score(diff)
        # return print("You Won")
    else:
        print("You Lost!!")



