#Import libraries
import random

playCheck = "Y" # Holds whether or not user wants to continue playing

# Loops while the user wants to continue playing
while playCheck != "N":

    # Initialize variables
    secretNumber = random.randint(1, 10) # User will try to guess this number

    userChances = 5

    userGuess = int(input("I am thinking of a number between 1 and 10.  You have " + str(userChances) + " guesses left. What's the number? "))


    # Loops until user guesses secretNumber
    while userGuess:
        userChances -= 1

        # Runs while user still has guesses remaining
        if userChances > 1:
            # Checks against secretNumber and returns if high, low, or same
            if userGuess == secretNumber:
                print("Yes! You win!")
                userGuess = ""
            elif userGuess < secretNumber:
                userGuess = int(input("Nope, " + str(userGuess) + " is too low.  You have " + str(userChances) + " guesses left. What's the number? "))
            elif userGuess > secretNumber:
                userGuess = (int(input("Nope, " + str(userGuess) + " is too high.  You have " + str(userChances) + " guesses left.  What's the number? ")))
        else:
            print("You ran out of guesses!")
            userGuess = ""

    playCheck = input("Do you want to play again (Y or N)? ")