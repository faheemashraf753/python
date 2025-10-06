# operators : operators are special symbols that perform specific operations on one or more operands (values or variables) and return a result.
# Python supports several types of operators, including:
# Arithmetic operators : These operators are used to perform mathematical operations such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
# Assignment operators : These operators are used to assign values to variables. They include the basic assignment operator (=) as well as compound assignment operators (+=, -=, *=, /=, etc.).
# Comparison operators : These operators are used to compare two values and return a boolean result (True or False). They include operators such as equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
# Logical operators : These operators are used to combine multiple boolean expressions and return a boolean result.

#note: e.g; 7 + 3 = 10 (7 and 3 are operands, + is operator and 10 is result)   

# arithmetic operators : (+, -, *, /, %, **, //)
a = 10
b = 5
print("Arithmetic Operators:")
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation
print("Floor Division:", a // b)   # Floor Division

# assignment operators : (=, +=, -=, *=, /=, %=, **=, //=)
x = 5
print("\nAssignment Operators:")
print("Initial value of x:", x)
x += 2
print("After x += 2:", x)    # now the value of x is 7 after this operation
x *= 3
print("After x *= 3:", x)    # now the value of x is 21 after this operation
x -= 4
print("After x -= 4:", x)    # now the value of x is 17 after this operation
x /= 2
print("After x /= 2:", x)    # now the value of x is 8.5 after this operation
x %= 3
print("After x %= 3:", x)    # now the value of x is 2.5 after this operation
x **= 2
print("After x **= 2:", x)   # now the value of x is 6.25 after this operation
x //= 2
print("After x //= 2:", x)   # now the value of x is 3.0 after this operation


# comparison operators : (==, !=, >, <, >=, <=) always return boolean value (true or false)
p = 7
q = 10
print("\nComparison Operators:")
print("p == q:", p == q)           # p Equal to q
print("p != q:", p != q)           # p Not equal to q
print("p > q:", p > q)             # p Greater than q
print("p < q:", p < q)             # p Less than q
print("p >= q:", p >= q)           # p Greater than or equal to q
print("p <= q:", p <= q)           # p Less than or equal to q


# logical operators : (and, or, not)
# and:
#true and true = true
#true and false = false
#false and true = false
#false and false = false
# or:
#true or true = true
#true or false = true
#false or true = true
#false or false = false
# not:
#not true = false
#not false = true


print("\nLogical Operators:")
m = True or False
print(m)
n = False and True
print(n)
o = not True
print(o)







# Python Operators Summary - Numbered List
# 1. Arithmetic Operators - 7 operators
#    Basic math operations: +, -, *, /, %, **, //

# 2.Comparison Operators - 6 operators
#   Value comparisons: ==, !=, >, <, >=, <=

# 3. Assignment Operators - 8+ operators
#    Variable assignments: =, +=, -=, *=, /=, %=, **=, //=

# 4. Logical Operators - 3 operators
#    Boolean logic: and, or, not

# 5. Identity Operators - 2 operators
#    Object identity: is, is not

# 6. Membership Operators - 2 operators
#    Sequence checks: in, not in

# 7. Bitwise Operators - 6 operators
#    Binary operations: &, |, ^, ~, <<, >>
