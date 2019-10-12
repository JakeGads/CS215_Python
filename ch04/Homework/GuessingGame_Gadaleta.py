"""
GuessingGame_Gadaeta.py

4.10 (GUESS THE NUMBER) Write a script that plays “guess the number.” 
Choose the number to be guessed by selecting a random integer in the range 1 to 1000. 
Do not reveal this number to the user. Display the prompt "Guess my number between 1 and 1000 with the fewest guesses:". 
The player inputs a first guess. If the guess is incorrect, display "Too high. Try again." or "Too low. Try again." 
as appropriate to help the player “zero in” on the correct answer, then prompt the user for the next guess. 
When the user enters the correct answer, display "Congratulations. You guessed the number!", and allow the user to choose whether to play again.

@author: Jake Gadaleta
"""

from random import randint


def check_guess(answer, guess):
    """This will check the guess of the user, returning if they were right and if they were too high or low"""

    if guess < answer:
        return False, "Too Low"  # the less than case
    elif guess > answer:
        return False, "Too High"  # the greater than case
    else:
        return True, ""  # the just right case


def game_loop():
    """This function allows us to restart the game itself over and over again"""
    correct = False  # sets it for false so the intaial loop will run
    answer = randint(1, 1000)  # get my random number

    while not correct:
        guess = int(input("Give me your guess:\t"))  # takes in the input

        correct, responce = check_guess(
            answer, guess
        )  # passes the answer and the guess to the checker expecting a boolean and a string back

        if not correct:  # gives some output if they were wrong
            print(responce, "Try Again")

    again = input(
        "Congrats you won\nEnter y to play again: "
    )  # win statment and asks the user if they would like to enter again

    if again == "y":
        game_loop()  # restarts teh loop, this makes a new number and restarts the game as well


if __name__ == "__main__":
    game_loop()  # this enters the loop, its in a fuction so I can run it recursivly
