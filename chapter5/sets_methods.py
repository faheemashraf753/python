# Methos  in sets :

# 1. Add() :    	Add single element
s = {4,52,54,41,544,22,14}

s.add(99999)
print(s, type(s))


# 2. Update() :     adding multiple elements 
w = {1, 9, 5, 4,3}
w.update([41,10,14,13,753])
print(w, type(w))


# 3. Clear() : delete whole set
print("\n clear set :")
x= {1,2,3,4,5,6}
x.clear()
print(x)


# 4. remove() : Remove element (error if missing)
z= {1,2,3,4,5,6}
z.remove(4)
print(z)

# 5. discard()	Remove element (no error)
m= {1,2,3,4,5,6}
m.discard(444)
print(m)



# 6. pop()	Remove random element
p= {1,2,3,4,5,6}
p.pop()
print(p)




#   operations in sets :
# 1. length() - find the total values in the set
f = {41,74,51,76,51,14, 14}    #output : 5 instead of 7 bcz no repeatation allowed in sets.
print(len(f))