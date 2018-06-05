# Set our import statements
import sys
import random

# Since we are going to be using an infinite loop, let's set a variable to watch
stop = False

# Welcome the user to the game and explain the rules
print('Welcome to our little rock paper scissors game!')
print('The rules are simple:')
print('Rock beats scissors')
print('Scissors beats paper')
print('Paper beats rock')

# Ask the user if they would like to play
begin = input('Would you like to play a game? <yes/no>: ')

# Set the value of begin to lower case to keep things standard
begin.lower()

# Check the value of begin and determine what to do next
while begin != 'yes':
    if begin == 'no':
        sys.exit(1)
    else:
        print('I\'m sorry. I didn\'t understand that input.')
        begin = input('Would you like to play a game? <yes/no>: ')
        begin.lower()

# Begin our infinite loop to keep the game going if the user would like to
while not stop:
    # Get the users choice for what they will play
    user_choice = input('Please select rock, paper, or scissors <rock/paper/scissors>: ')

    # Set the value of user_choice to lower case to keep things standard
    user_choice = user_choice.lower()

    # Create a list with the possible computer choices
    possible_computer_choices = ['rock', 'paper', 'scissors']

    # Select a random option from the possible computer choices list
    computer_choice = random.choice(possible_computer_choices)

    # Compare the users choice and the computers choice and determine the result
    if computer_choice == user_choice:
        print('Tie game!')
    elif computer_choice == 'rock' and user_choice == 'paper':
        print('You chose: paper!')
        print('The computer chose: rock!')
        print('You win!')
    elif computer_choice == 'rock' and user_choice == 'scissors':
        print('You chose: scissors!')
        print('The computer chose: rock!')
        print('Computer wins!')
    elif computer_choice == 'paper' and user_choice == 'rock':
        print('You chose: rock!')
        print('The computer chose: paper!')
        print('Computer wins!')
    elif computer_choice == 'paper' and user_choice == 'scissors':
        print('You chose: scissors!')
        print('The computer chose: paper!')
        print('You win!')
    elif computer_choice == 'scissors' and user_choice == 'rock':
        print('You chose: rock!')
        print('The computer chose: scissors!')
        print('You win!')
    elif computer_choice == 'scissors' and user_choice == 'paper':
        print('You chose: paper!')
        print('The computer chose: scissors!')
        print('Computer wins!')
    else:
        print('I\'m sorry. I didn\'t understand that input.')

    # Ask the user if they would like to play another game
    play_again = input('That was fun! Would you like to play another game? <yes/no>: ')

    # Set the value of play_again to lower case to keep things standard
    play_again = play_again.lower()

    # Check the value of play_again and determine what to do next
    while play_again != 'yes':
        if play_again == 'no':
            print('Thanks for playing!')
            sys.exit(1)
        else:
            print('I\'m sorry. I didn\'t understand that input.')
            play_again = input('That was fun! Would you like to play another game? <yes/no>: ')
            play_again.lower()
