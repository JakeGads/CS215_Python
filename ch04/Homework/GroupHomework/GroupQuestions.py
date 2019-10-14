"""

authors: Maggie Arnold and Jake Gadaleta
"""
# Jake's special imports
from subprocess import call # lets me run terminal commands
from platform import system # lets me check what OS python is running on
from time import sleep

# For random
from random import randrange

def clearScreen():
    """Tap into the OS to clear a terminal window"""
    sleep(1)
    if system == 'Windows':
        clear = 'cls'
    else:
        clear = 'clear'

    call(clear, shell=True)

def drawBox(t_score, h_score):
    """Draws the actual box"""
    print("[", end="")

    for i in range(70):
        if i == t_score == h_score:
            print("Ouch!!!", end="")
            for i in range(70 - i - len("Ouch!!!")):
                print("-", end="")
            break
            
        elif i == t_score:
            print('T', end="")

        elif i == h_score:
            print("H", end="")

        else:
            print("-", end="")

    print("]")

def t_scorer(number):
    if number < 5:
        return 3
    elif 5 < number < 7:
        return -6
    else:
        return 1


def h_scorer(number):
    if number < 2:
        return 0
    elif 2 < number < 4:
        return 9
    elif 4 < number < 5:
        return -12
    elif 5 < number < 8:
        return 1
    else:
        return -2

# Maggie don't freak out this is for me
if __name__ == "__main__":
    h_score = 0
    t_score = 0
    winner = False

    while not winner:
        h_score += h_scorer(randrange(0,10))
        t_score += t_scorer(randrange(0,10))
        
        clearScreen()

        if h_score < 0:
            h_score = 0
        if t_score < 0:
            t_score = 0

        if h_score >= 70:
            h_score = 69
            print("Hare Won")
            winner = True
        if t_score >= 70:
            t_score = 69
            print("Tortoise Won")
            winner = True
        
        drawBox(t_score, h_score)