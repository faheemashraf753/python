# functions and methods in lists:



# 1. Adding elements to a list
fruits = ['apple', 'banana']

fruits.append('cherry')        # ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')     # ['apple', 'orange', 'banana', 'cherry']
fruits.extend(['grape', 'kiwi']) # ['apple', 'orange', 'banana', 'cherry', 'grape', 'kiwi']

print(fruits)



# 2. Removing elements from a list
numbers = [1, 2, 3, 2, 4, 5]

numbers.remove(2)              # [1, 3, 2, 4, 5] (removes first occurrence)
popped = numbers.pop()         # [1, 3, 2, 4], popped=5 bydefault last element
popped2 = numbers.pop(1)       # [1, 2, 4], popped2=3
numbers.clear()                # [] (empties list)  and all the above operations can not be done after this because list is empty now and lists are mutable so it will delete all the references of that list.

print(numbers)
print(popped, popped2)


# 3. Searchig and information :
colors = ['red', 'blue', 'green', 'blue']

index = colors.index('red')   # 0 (first occurrence)
count = colors.count('blue')   # 2 (number of occurrences)
length = len(colors)           # 4 (number of elements)
exists = 'red' in colors       # True (membership check)

print(index, count, length, exists)



# 4. Sorting & Reordering
numb = [3, 1, 4, 1, 5]

numb.sort()
print("asc :", numb)                 # [1, 1, 3, 4, 5]

numb.sort(reverse=True)
print("des :", numb)                 # [5, 4, 3, 1, 1]

numb.reverse()
print("rev :", numb)                 # [1, 1, 3, 4, 5]

sorted_nums = sorted(numb)
print("sorted:", sorted_nums)        # New sorted list


# useful builtin functions
nums = [2, 5, 1, 8, 3]

maximum = max(nums)            # returns : 8
minimum = min(nums)            # returns: 1
total = sum(nums)              # rreturns :19
any_true = any([False, True, False])  # True
all_true = all([True, True, False])   # False
print(maximum, minimum, total, any_true, all_true)



# Quick Reference - Most Used Methods:
# ADD:    append(), insert(), extend()
# REMOVE: remove(), pop(), clear()
# SEARCH: index(), count(), in operator
# SORT:   sort(), sorted(), reverse()
# COPY:   copy(), list(), [:]
# INFO:   len(), max(), min(), sum()