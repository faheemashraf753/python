# string : string data type is used to store sequences of characters, such as words or sentences. Strings are enclosed in single or double quotes or triple quotes for multi-line strings.
# we can write string in three ways:
# 1. single quotes eg 'hello'
# 2. double quotes eg "hello"
# 3. triple quotes eg '''hello''' or """hello""" (used for multi-line strings)

#strings are immutable (cannot be changed) but we can perform various operations on strings.

name = "John Doe"   # string in double quotes
#indexing in string starts from 0 to n-1 (n is length of string)
print("the element in the 0 position :",name[0])      # prints 'J'
print("the element in the 1 position :",name[1])      # prints 'o'
print("the element in the 2 position :",name[2])      # prints 'h'
print("the element in the 3 position :",name[3])      # prints 'n'
print("the element in the 4 position :",name[4])      # prints ' ' (space)
print("the element in the -1 position :",name[-1])     # prints 'e' (last character)
print("the element in the -2 position :",name[-2])     # prints 'o' (second last character)
print("the element in the -3 position :",name[-3])     # prints 'D' (third last character)

#length of string:
print("the total length of the string is :",len(name))    # that prints 8 (length of string) means that all characters in the string including space.

#slicing in string:
print("the slicing of string from 0 to 4 is :",name[0:4])   # prints 'John' (from index 0 to 3, 4 is excluded)
print("the slicing of string from 5 to end is :",name[5:])   # prints 'Doe' (from index 5 to end)
print("the slicing of string from start to 4 is :",name[:4])   # prints 'John' (from start to index 3, 4 is excluded)
print("the slicing of string from -3 to end is :",name[-3:])   # prints 'Doe' (from index -3 to end)
print("the slicing of string from start to -3 is :",name[:-3])   #  prints 'John ' (from start to index -4, -3 is excluded)
print("the slicing of string from 0 to 7 with step 2 is :",name[0:7:2])   # prints 'Jh o' (from index 0 to 6 with step 2)
print("the slicing of string from start to end with step 2 is :",name[::2])   # prints 'Jh o' (from start to end with step 2)
print("the slicing of string from end to start with step -1 is :",name[::-1])   # prints 'eoD nhoJ' (from end to start with step -1, this reverses the string)
print("the slicing of string from end to start with step -2 is :",name[::-2])   # prints 'e nJ' (from end to start with step -2)
print("the slicing of string from 7 to 0 with step -1 is :",name[7:0:-1])   # prints 'eoD nho' (from index 7 to 1 with step -1, 0 is excluded)
print("the slicing of string from 7 to 0 with step -2 is :",name[7:0:-2])   # prints 'e n' (from index 7 to 1 with step -2, 0 is excluded)
print("the slicing of string from -1 to -8 with step -1 is :",name[-1:-8:-1])   # prints 'eoD nhoJ' (from index -1 to -7 with step -1, this reverses the string)
print("the slicing of string from -1 to -8 with step -2 is :",name[-1:-8:-2])   # prints 'e nJ' (from index -1 to -7 with step -2)
