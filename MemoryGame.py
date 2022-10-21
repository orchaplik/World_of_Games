from random import randrange
import Live
import time
import os


def generate_sequence(diff):
    list_of_nums = []
    i = 1
    while i <=  int(diff):
        list_of_nums.append(int(randrange(1,101)))
        i = i + 1
    print(list_of_nums)
    time.sleep(0.7)
    os.system('cls')
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
    return generate_sequence(diff) == get_list_from_user(diff)


def play(diff):
    print(is_list_equal(diff))



