# Ask the user for a number to check and see if it is even or odd.
number = int(input('Please enter a number: '))

# Check to see if the number is even or odd and output the appropriate message.
if number % 2 == 0:
    print('The number "' + str(number) + '" is even.')
else:
    print('The number "' + str(number) +'" is odd.')

# Check to see if the number is multiple of four and print a message.
if number % 4 == 0:
    print('The number "' + str(number) + '" is a multiple of four.')
else:
    print('The number "' + str(number) + '" is not a multiple of four.')