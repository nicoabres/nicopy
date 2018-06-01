# Ask the user for a string so we can test if it is a palindrome or not.
user_string = input('Please enter a string: ')

# Reverse the string that the user entered and store it in a variable for later
reversed_user_string = user_string[::-1]

# Check to see if the string the user entered, and the reverse, are the same
if reversed_user_string.lower() == user_string.lower():
    print('This is a palindrome!')
else:
    print('This is not a palindrome!')