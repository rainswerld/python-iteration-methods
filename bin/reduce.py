from functools import reduce

# reduce iterates and works with each element as well as an "accumulator"
# The accumulator can start as a provided value or as the first element
# https://docs.python.org/3/library/functools.html#functools.reduce
# reduce( function, iterable, optional_accumulator_start_value )

# Add all numbers together
nums = [0, 1, 2, 3, 4]
#  should start with 0

# Multiply all numbers together
nums = [0, 1, 2, 3, 4]
#  should start with 1

# Convert into a dictionary
string = 'Hello World'
# Write a named function `strToDict` that will be used by `reduce`
# to convert the string into a dictionary of characters and their counts
# Ex: { 'H': 1, 'e': 1, 'l': 3, 'o': 2, 'W': 1, 'r': 1, 'd': 1 }
# Can we do this with lambda? Yes but it's messier: https://stackoverflow.com/questions/1585322/is-there-a-way-to-perform-if-in-pythons-lambda
# Readability is key!
