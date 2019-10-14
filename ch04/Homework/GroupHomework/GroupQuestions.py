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

    print("]", end="")



# Maggie don't freak out this is for me
if __name__ == "__main__":
    debug = True

    if debug:
        drawBox(5,5)
        print()
        drawBox(1,2)
    print()