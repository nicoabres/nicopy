# Define a function to get the a users number which we will check
def get_number():
    user_number = input('Please enter a number: ')
    return user_number

# Define a function to check if the input the user entered is actually a number
def check_if_number(user_number):
    if user_number.isnumeric():
        return True
    else:
        return False

# Define a function to check if the input is prime or not
def check_if_prime(user_number):
    if int(user_number) % 2 == 0 and int(user_number) > 2:
        print('The number: ' + str(user_number) + ' is not prime!')
    else:
        print('The number: ' + str(user_number) + ' is prime!')

# Get the users number using our "get_number" function
user_number = get_number()

# Check if the users number is actually a number and store the result
is_number = check_if_number(user_number)

# If the users number is actually a number, check if it's prime. If it's not a number, ask again.
if is_number:
    check_if_prime(user_number)
else:
    while is_number is False:
        user_number = input('The entry you entered is not a number. Please try again: ')
        is_number = check_if_number(user_number)
    check_if_prime(user_number)