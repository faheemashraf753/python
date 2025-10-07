# functions and methods in tuples:

tup = (1, "apple", 3.14, True , "banana")
print(tup)


# Tuple Methods (Only 2 Available):
# 1. count() - Count Occurrences
# Count how many times a value appears
numbers = (1, 2, 3, 2, 4, 2, 5)

print(numbers.count(2))    # Output: 3
print(numbers.count(1))    # Output: 1
print(numbers.count(6))    # Output: 0 (not found)

# With strings
fruits = ('apple', 'banana', 'apple', 'orange')
print(fruits.count('apple'))  # Output: 2


# 2. index() - Find Position
# Find the first occurrence of a value
number = (10, 20, 30, 20, 40)

print(number.index(20))    # Output: 1 (first occurrence)
print(number.index(30))    # Output: 2

# With optional start and end parameters
print(number.index(20, 2)) # Output: 3 (search from position 2)

# Error if value not found
# print(numbers.index(50))   # ❌ ValueError: tuple.index(x): x not in tuple