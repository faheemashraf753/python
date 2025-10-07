# Sets :
# Unordered - No index positions
# Mutable - Can add/remove items
# Unique elements - No duplicates allowed/ No repeated elemnt allowed (set connot cannot repeated values)
# Unhashable elements - Can't contain lists/dicts
# use of small braces - {}  or set([...])

# e.g:Creation of a set
# method 1 :
sett = {44, 66, 77, 74, 666,12}
print(sett)
print(type(sett))
# method 2:
s = set([44,5,55,56,65])
print(s)
print(type(s))


# empty set :
print("\n empty set :")
ss = set()
print(ss)
print(type(ss))



# reated elements :
rep = set()
rep = {44,41,47,15,15,15, 15, 41, 41, 14, 15}            #output : {41, 44, 15, 14, 47} -No repeated value and no order matters in the sets.
print(rep)
print(type(rep))


# set strings :
w = set()
w = {"apple", "mango", "papaya", "apple", "mango", "nanana"}
print(w)
print(type(w))


# Mixed data types are fine:
my_set = {1, "hello", 3.14, True, (1, 2, 3)}
print(my_set)  # {1, 3.14, (1, 2, 3), 'hello'}