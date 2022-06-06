#! /usr/bin/env python3

"""Game where the goal is to guess the number"""

from random import *
from math import *
import os
import time


def init():
    """
    handle the init of the game :
    get the name of the player
    set the difficulty
    set range of numbers
    :return: name of the player, range of numbers, difficulty
    :rtype: str, int, int
    """
    print("Hello ! What is your name ?")
    name = input()
    difficulty = -1
    while not (1 <= difficulty <= 3):
        print(f"Well {name}, choose the difficulty between 1 and 3.")
        difficulty = input_num()
    max_value = 0
    while max_value < 1:
        print("Okey, then choose the max value of the number to guess:")
        max_value = input_num()

    return name, difficulty, max_value


def god_of_war(difficulty, max_value):
    """
    Define the number of try needed to win according the number and the difficulty set
    :param difficulty: int between 1 and 5
    :param max_value: int between 0 and +inf
    :return: number(int) of try
    """
    nb_try = floor(log(max_value, 2)) + 1
    if difficulty == 1:
        return max_value//2
    elif difficulty == 2:
        return nb_try
    else:
        return nb_try//2 + 1


def guess(nb_try, max_value):
    """
    fonction qui guess la valeur
    :param nb_try:
    :param max_value:
    :return:
    """
    value = randint(1, max_value)
    tried = 0
    while tried < nb_try:
        print(f"Guess the number between 1 and {max_value}, you have {nb_try - tried} try left.")
        guessed = input_num()
        if guessed == value:
            print("Wait for it, you...")
            time.sleep(2)
            os.system("clear")
            print("WIN!!!")
            return
        if guessed < value:
            os.system("clear")
            print(f"The value to guess is superior than {guessed}")
        elif guessed > value:
            os.system("clear")
            print(f"The value to guess is inferior than {guessed}")
        tried += 1
    print("Wait for it, you.....")
    time.sleep(2)
    os.system("clear")
    print(f"FAIL! The value was {value}")


def input_num():
    """
    fonction qui recupere une valeur donner dans le terminal et renvoie son entier
    si un entier n'est pas rentré, une nouvelle demande est lancée
    :return:
    """
    value = input()
    while not value.isnumeric():
        print("Veuillez rentrez un caractère valide")
        value = input()
    return int(value)


def main():
    """main function"""
    name, difficulty, max_value = init()
    max_try = god_of_war(difficulty, max_value)
    guess(max_try, max_value)


if __name__ == '__main__':
    main()
