# datatypes : Datatypes are used to store different types of data in variables.
# Python has several built-in data types, including:
# int : Integer data type is used to store whole numbers (both positive and negative) without decimal points.
# float : Float data type is used to store numbers with decimal points (both positive and negative
# str : String data type is used to store sequences of characters, such as words or sentences. Strings are enclosed in single or double quotes.
# bool : Boolean data type is used to store one of two values: True or False.
#none : None data type is used to represent the absence of a value or a null value.


a = 5           #int
b = 3.14        #float
c = "Hello"     #str
d = True        #bool
e = None       #none
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# You can also use the type() function to check the data type of a variable.

print("converting the value of data types :")
# You can also convert between different data types using built-in functions such as int(), float(), str(), and bool().
x = 10         #int
y = float(x)   #convert int to float
z = str(x)     #convert int to str
w = bool(x)    #convert int to bool (0 is false, any non-zero value is true)
print("the value of y :",type(y))
print("the value of z :",type(z))
print("the value of w :",type(w))
# Note: Converting a float to an int will truncate the decimal part (not round it).


#  Quick Reference Chart: Can Convert TO:
#   FROM    →   int   float   str   bool   complex
#   int     ✓     ✓     ✓     ✓       ✓
#   float   ✓     ✓     ✓     ✓       ✓  
#   str     ✓*    ✓*    ✓     ✓       ✓*
#   bool    ✓     ✓     ✓     ✓       ✓
#   complex ❌    ❌     ✓     ✓       ✓
#   Key: ✓ = Always works, ✓* = Works only if valid format, ❌ = Never works