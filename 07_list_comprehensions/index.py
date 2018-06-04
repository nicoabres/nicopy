# Specify a list that we will use to pull the even numbers out of.
a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using list comprehension, iterate through the numbers in the list and pull out only the even numbers.
evens = [number for number in a_list if number % 2 == 0]
print(evens)
