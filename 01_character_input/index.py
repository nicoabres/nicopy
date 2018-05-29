# Import datetime to get the current year
import datetime

# Ask the user to enter their name and print it out.
name = input('Please enter your name: ')
print('Your name is: ' + name)

# Ask the user to enter a number so that we can print their name that many times.
number = int(input('Please enter a number: '))
print('You choose number: ' + str(number))

# Use a for loop to print the name of the user.
for i in range(number):
    print(name)

# Ask the user to enter their age and print it out.
age = int(input('Please enter your age: '))
print('Your age is: ' + str(age))

# Get the current year so we can determine what year the user will be 100 years old.
now = datetime.datetime.now()
current_year = int(now.year)
print('It is currently year: ' + str(current_year))

# Do some math so we can tell the user what year it will be when they turn 100
year_at_100 = (current_year - age) + 100

# Tell the user what year they will turn 100
print('You will turn 100 in year: ' + str(year_at_100))
