# Ask a user for a number that we will use to get all divisors of
number = int(input("Please enter a number: "))

# Generate a list of number that could be "possible" divisors
range_list = range(1, number+1)

# Iterate through the list and find what numbers are divisors of the users number.
for item in range_list:
    if number % item == 0:
        print(item)
    else:
        pass
