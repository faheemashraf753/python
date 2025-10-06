# this program takes two numbers as input as string from the user and concatenates them instead of summing them.
a = input("enter number 1: ")
b = input("enter number 2: ")

print("number 1 is:", a)
print("number 2 is:", b)

print("the (concat)sum of a & b is:", a + b)  # this will concatenate the two inputs as strings and sum not
#for upper code we can give any type of input like string or float or int but it will take as string only and concatenate them.



# To fix this, we need to convert the inputs to integers or floats before summing them.
x = int(input("enter number 1: "))
y = int(input("enter number 2: "))

print("number 1 is:", x)
print("number 2 is:", y)

print("the sum of two numbers x & y is:", x + y)  # this will sum the two inputs as integers and give the correct result
# we can only give integer type input otherwise it will give error.