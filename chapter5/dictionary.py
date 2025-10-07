# Dictionary : A collection of key-value pairs, where each key is unique.
# Dictionaries are defined using curly braces {}.
# Example: my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# Keys must be immutable types (like strings, numbers, or tuples).
# Values can be of any data type and can be duplicated.
# Dictionaries are mutable, meaning you can change, add, or remove items.
# imp.: Accessing values is done using keys, not indices.

# properties of dictionaries : it is
# 1. unordered  2. mutable  3. indexed  4. cannot contain duplicate keys.


# Example dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Math", "Science"]
}
print(my_dict)
print(type(my_dict))


# Accessing values
print(my_dict["name"])        # Output: Alice  



d = {}  #empty ditionary 
print("d :", d)
print(type(d))