# Import random module so we can generate two random number lists
import random

# Generate two lists, each with a random set of numbers.
list_a = random.sample(range(1, 101), random.randint(1, 21))
list_b = random.sample(range(1, 101), random.randint(1, 51))

# Print out the lists just to make sure they are random and different sizes
print(list_a)
print(list_b)

# Check to see which list is longer and use that one to iterate through first
if len(list_a) > len(list_b):
    longest_list = list_a
    shortest_list = list_b
else:
    longest_list = list_b
    shortest_list = list_a

# Iterate through longest list while comparing it to the shortest list
new_list = []
for number_a in longest_list:
    for number_b in shortest_list:
        if number_a == number_b:
            new_list.append(number_a)

print(set(new_list))
