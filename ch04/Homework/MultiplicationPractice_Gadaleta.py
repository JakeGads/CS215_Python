"""
MultiplicationPractice_Gadaleta.py
Tests children on simple multiplication
author: Jake Gadaleta
"""
from random import randint # allows me to do the random inclusivly

def generate_numbers():
    """returns a tuple of random numbers"""
    return (randint(1, 9), randint(1,9))

def generate_question(*args):
    """looks for the user to enter the correct number as presented"""
    answer = args[0] * args[1] # calcualtes the correct answer

    user = answer + 1 # makes user ! answer

    # main while loop
    while user is not answer:
        # takes in the input from the user
        user = int(input(f"How much is {args[0]} times {args[1]}?\t"))

        # checks the users answer and reall
        if user is not answer:
            print("No. Please try again.")
        else:
            print("Very good!")

def main():
    # sets a starting value
    play = "y"

    # checks for both y and yes (I did lower this time)
    while play.lower() == "y"or play.lower() == "yes":
        # eneters my game loop, and also generates my numbers
        generate_question(*generate_numbers())
        # enters the loop again
        play = input("Enter \"y\" to play again\t")

if __name__ == "__main__":
    main()