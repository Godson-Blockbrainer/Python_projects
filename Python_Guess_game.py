#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is going to be a simple guessing game where the computer will generate a random number between 1 to 100, and the user has to guess it in 9 attempts.
#Based on the user's guess, the  computer will give various hints if the number is 
#high or low. When the user guess matches the number computer will print the answer along with the number of attempts. You have to make the 
#submission by uploading your github link to your repositories where you must have 
#pushed your codes.

# We are going to use a package that contains a function that can generate randome numbers
import random

# now we will tell the package to pick  a number between 1- 100 and asigng a variable to store this unknown value 
number_to_guess = random.randint(1, 100)

# attempts is a variable that will help us store and monitor the number of gueses, for now the user hasnt made any guess so its zero .
attempts = 0

# Using the while loop statement to start the game which will continue looping until the player guesess upto 9 times
while attempts < 9:

    # guess stores the input collected from user and (int) converts it to interger
    guess = int(input("Guess a number between 1 and 100: "))

 # on any input by the user, the attempts variable automatically records a new entry thereby adding to the initial number of attempts   
    attempts += 1. 

    # this will check how close the user input is to the computers generated number 
    difference = guess - number_to_guess

    # Check if the guess is too high, too low, or just right
    if difference < 0:
        print("Too low!")
    elif difference > 0:
        print("Too high!")
    else:
        print("You got it!")
        print("Number of attempts: ", attempts)
        break

# Check if the maximum number of attempts was reached
if attempts == 9:
    print("Sorry, you didn't guess the number. The number was: ", number_to_guess)


# In[ ]:




