# Set our import statements
import random           # Used to randomly generate a number

# Generate a list of random numbers (taken from exercise five)
list_a = random.sample(range(1, 101), random.randint(1, 21))

# Create a function to pull the first and last elements out of a list
def pull_elements(list):
    first_last = [list[0], list[-1]]
    return first_last

# Print out the random list
print(list_a)

# Use the function to get the first and last elements
first_last = pull_elements(list_a)

# Print the new list
print(first_last)