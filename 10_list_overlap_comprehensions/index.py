# Set our import statements
import random           # Used to randomly generate a number

# Generate our two random lists (taken from exercise five)
list_a = random.sample(range(1, 101), random.randint(1, 21))
list_b = random.sample(range(1, 101), random.randint(1, 51))

# Check to see which list is longer and use that one to iterate through first (taken from exercise five)
if len(list_a) > len(list_b):
    longest_list = list_a
    shortest_list = list_b
else:
    longest_list = list_b
    shortest_list = list_a

# Print the two lists so we can see which ones might be common
print(longest_list)
print(shortest_list)

# Use list comprehension to find the common numbers
common_numbers = set([i for i in longest_list if i in shortest_list])

# Print the comon numbers list
print(common_numbers)