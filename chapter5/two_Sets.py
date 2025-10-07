#1. Union of 2 sets :
s1 = {1, 5, 9}
s2 = {3, 5, 7}

s3 = s1.union(s2)
print(s3)

# or print(s1.union(s2))


# 2. Intersection of 2 sets :
s10 = {9, 6, 5, 3, 4}
s11 = {7, 4, 5, 6, 1}

print(s10.intersection(s11))        # output : {4, 5, 6}



# 3. is_Subset
s20 = {10, 12, 14, 16}
s21 = {10, 12, 14, 16, 18, 20}

print(s20.issubset(s21))  # True - all elements of s20 are in s21


# 4. difference() :
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Method 1: difference()
print(A.difference(B))      # {1, 2, 3}

# Method 2: - operator  
print(A - B)               # {1, 2, 3}

# Order matters!
print(B.difference(A))      # {6, 7, 8}
print(B - A)               # {6, 7, 8}