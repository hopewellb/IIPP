# Baby's First "Guess the Number"

import simplegui
import random
import math

# global variables
secret_number = 100
num_range = 100
number_of_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number
    global number_of_guesses
    global num_range
    # sets secret number and guesses
    secret_number = random.randrange(0, num_range)
    if num_range == 100:
        number_of_guesses = 7
    else:
        number_of_guesses = 10
    print "New game started. Range is from 0 - " + str(num_range)
    print "Number of remaining guesses is " + str(number_of_guesses) + "\n"
    
# event handlers
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global num_range
    global number_of_guesses
    num_range = 100
    number_of_guesses = 7
    new_game()
  
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global num_range
    global number_of_guesses
    num_range = 1000
    number_of_guesses = 10
    secret_number = random.randrange(0, num_range)
    new_game()

# game logic   
def input_guess(guess):
    global secret_number
    global number_of_guesses
    print "Guess was " + guess 
    guess = int(guess)
    # controls number of guesses
    number_of_guesses = number_of_guesses - 1 
    # guess logic
    if guess == secret_number:
        print "Correct!\n"
        new_game()
    elif guess > secret_number:
        print "Number of remaining guesses is " + str(number_of_guesses)
        print "Lower!\n"
    else:
        print "Number of remaining guesses is " + str(number_of_guesses)
        print "Higher!\n"
   
    if number_of_guesses == 0:
        print "Out of guesses! The correct number was " + str(secret_number)
        new_game() 
        
# create frame
f = simplegui.create_frame("Guess the Number!", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
