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

def drawBox(animal, score, size=70):
    """This will print one line with the animals current location on it"""
    string = '['
    for i in range(size):
        if score is i:
            string += animal
        else:
            string += '-'
    string += ']'
    return string
    



# Maggie don't freak out this is for me
if __name__ == "__main__":
    debug = True

    if debug:
        for i in range(randrange(100)):
            clearScreen()
            print("Round # ", i )
            print(drawBox('H', randrange(70)))
            print(drawBox('T', randrange(70)))