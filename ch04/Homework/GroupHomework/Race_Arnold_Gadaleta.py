"""
Race_Arnold_Gadaleta.py
Emulates the Tortoise and the Hare race
authors: Maggie Arnold and Jake Gadaleta
"""

# Jake's special imports
from subprocess import call  # lets me run terminal commands
from platform import system  # lets me check what OS python is running on
from time import sleep

# For random
from random import randrange


def clearScreen():
    """Tap into the OS to clear a terminal window"""
    sleep(0.5)  # takes a brief pause before clearing the screen
    if system == "Windows":  # test to see if the system is windows
        clear = "cls"  # set it to the windows command
    else:
        clear = "clear"  # sets the unix and linux commands

    call(clear, shell=True)  # clears the current shell


def drawBox(t_score, h_score):
    """Draws the actual box"""
    print("[", end="")  # prints my open bracket

    for i in range(70):  # the size is 70
        if (
            i == t_score == h_score
        ):  # checks to see if h and t are both at i at the same time
            print("Ouch!!!", end="")  # prints out the Ouch
            for i in range(70 - i - len("Ouch!!!")):  # handles the rest of the --
                print("-", end="")
            break

        elif i == t_score:  # handles where t is
            print("T", end="")

        elif i == h_score:  # handles where h is
            print("H", end="")

        else:  # handles where neither are true
            print("-", end="")

    print("]")  # prints an end bracket


def t_scorer(number):
    """scores the totoise based on what was provided in the book"""
    # defined function to calculate the score for the Tortoise
    if number < 5:
        return (
            3
        )  # checks if it meets the criteria and moves the Tortoise 3 spaces to the right
    elif 5 < number < 7:
        return (
            -6
        )  # checks if it meets the criteria and moves the Tortoise 6 spaces to the left
    else:
        return (
            1
        )  # if neither of the above statements are true it moves the Tortoise 1 space to the right


def h_scorer(number):
    """scores the hare based on what was provided by the book"""
    # runs the predefined sections as they are raised to the 10th
    if number < 2:
        return 0  # does not move the hare to simulate him taking a nap
    elif 2 < number < 4:
        return 9  # moves the hare 9 spaces to the right on the track
    elif 4 < number < 5:
        return -12  # moves the hare 12 spaces to the left on the track
    elif 5 < number < 8:
        return 1  # moves the hare over 1 space to the right
    else:
        return (
            -2
        )  # if all the above is not true the hare will move 2 spaces to the left


if __name__ == "__main__":
    # setting out initial values
    h_score = 0
    t_score = 0
    winner = False

    # runs until a winner is found
    while not winner:
        # find my next random score and add it back to t and h
        h_score += h_scorer(randrange(0, 10))
        t_score += t_scorer(randrange(0, 10))

        # wipes my screen
        clearScreen()

        # resets the values of T and H if they leave the range
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

        # redraws my box
        drawBox(t_score, h_score)
