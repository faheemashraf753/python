# list : lists in python are like container to store any type of data 
# e.g; list = ["apple", "football", 42, False, 75.41, "good_boy"]
# lists are mutable and can be changed.
# list are fully flexible that means 1. you can change it. 2. you can add more data where you want in start, middle or in the end. 3. you can remove data any where. 

demo_list = ["apple", "football", 42, False, 75.41, "good_boy"]
print(demo_list[0])

demo_list[0]= "bananaaaah"             #unlike strings lists are mutable.
print(demo_list[0])

print(demo_list)


# indexing in lists  :
# positive indexing
print("-----positive indexing :")
print(demo_list[0])      # first element
print(demo_list[4])      # second element
# print(demo_list[8])      # IndexError: list index out of range

# negative indexing
print("-----negative indexing :",)
print(demo_list[-1])     # last element
print(demo_list[-3])     # third last element
print(demo_list[-6])     # first element


# slicing in lists :
print("-----slicing in lists :",)
print(demo_list[0:3])    # ['bananaaaah', 'football', 42] 
print(demo_list[2:5])    # [42, False, 75.41]
print(demo_list[:4])     # ['bananaaaah', 'football', 42, False]
print(demo_list[3:])     # [False, 75.41, 'good_boy']
print(demo_list[:])      # ['bananaaaah', 'football', 42, False, 75.41, 'good_boy']
print(demo_list[-4:-1])  # [42, False, 75.41]
print(demo_list[-3:])    # [False, 75.41, 'good_boy']
print("steps",demo_list[::2])   # ['bananaaaah', 42, 75.41]