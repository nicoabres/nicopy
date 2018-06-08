# Set our import statements
import sys              # Used to exit gracefully
import random           # Used to randomly generate a number

# Welcome the user to the game, just like we did in exercise number eight
print('Welcome to the best guessing game on the internet!')
print('The rules are even more simple than rock, paper, scissors:')
print('The computer will generate a random number, between 1 and 9, and you will have to guess it.')
print('The computer will tell you if you are higher or lower!')
print('The game is over once you successfully guess the right number.')
print('Good luck!')

# Print a separator to make it a little more clear when the game starts
print('-------------------- START --------------------')

# Set a variable to hold the number the computer randomly guesses
computers_number = random.randint(1, 9)
print('The computer has choosen its number!')

# Set a variable and start a loop to keep the game going until the player says to stop
stop = False
while not stop:
    # Prompt the user to enter a number that they think the computer chose
    players_number = input('Please enter the number you think the computer chose, or type "exit" to end the game: ')

    # Check to see if the number enderd by the user is actually a number
    numberCheck = True
    while numberCheck:
        if players_number.isnumeric():
            players_number = int(players_number)
            if players_number > 9:
                players_number = input('The number you entered was too high, please enter a new number: ')
            elif players_number == 0:
                players_number = input('You cannot choose the number "0", please enter a new number: ')
            else:
                numberCheck = False
        elif players_number.lower() == 'exit':
            print('Thank you for playing!')
            sys.exit(1)
        else:
            players_number = input('You didn\'t seem to enter a number, please enter a new number: ')

    print('You have guessed: ' + str(players_number))

    # Check if the number is higher, lower, exact, or if the user wants to stop
    if computers_number > players_number:
        print('The computer\'s number is higher, try again!')
    elif computers_number < players_number:
        print('The computer\'s number is lower, try again!')
    else:
        print('Congrats! You win! The computer\'s number was: ' + str(computers_number))
        stop = True
