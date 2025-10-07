# string functions : 

# 1. Case Conversion Functions
text = "Hello World Python"

print(text.upper())       # HELLO WORLD PYTHON
print(text.lower())       # hello world python  
print(text.title())       # Hello World Python
print(text.capitalize())  # Hello world python
print(text.swapcase())    # hELLO wORLD pYTHON


# 2. Search & Find Functions
z = "Python programming is fun"

print(z.find('pro'))        # 7 (index where found). Find where 'pro' starts
print(z.index('pro'))       # 7 (similar to find). finds 'pro' and returns index
print(z.rfind('n'))         # 23 Finds last 'n'. returns index of last 'n' which is 23 (n-1)
print(z.count('n'))         # 3 (number of occurrences). Counts 'n' occurrences

# 3.  Check & Validation Functions

x1 = "Hello123"
x2 = "HELLO"
x3 = "hello"
x4 = "123"
x5 = "   "

print(x1.isalnum())    # True (letters/numbers only) because it contains both letters and numbers
print(x2.isalpha())    # True (letters only) because it contains only letters
print(x4.isdigit())    # True (numbers only) because it contains only numbers
print(x4.isnumeric())  # True (numbers only) because it contains only numbers
print(x3.islower())    # True (letters are lowercase) because all letters are lowercase
print(x2.isupper())    # True (letters are uppercase) because all letters are uppercase
print(x5.isspace())    # True (whitespace only) because it contains only spaces
print(x1.istitle())  # True (title case) because it starts with uppercase followed by lowercase letters
print(x1.__contains__('123'))  # True (contains substring) because it contains '123'

# 4.  Formatting & Cleaning Functions
m = "   hello world   "

print(m.strip())        # "hello world" (remove spaces) it removes spaces from both sides
print(m.lstrip())       # "hello world   " (left only) it removes spaces from left side only
print(m.rstrip())       # "   hello world" (right only) it removes spaces from right side only

n = "john"
print(n.center(10, '-'))  # --john--- (center with -) 10 means total length of string will be 10 and it will center the string with '-' on both sides
print(n.ljust(10, '*'))   # john****** (john followed by 6 '*') and it will left justify the string with '*' on right side as the total length is 10
print(n.rjust(10, '*'))   # ******john (right justify with *) and it will right justify the string with '*' on left side as the total length is 10


# 5. Split & Join Functions
words = "apple,banana,cherry"

# Split into list
fruits = words.split(',')   # ['apple', 'banana', 'cherry'] it splits the string into a list wherever there is a comma
print(words)

# Join list into string
new_text = '-'.join(fruits) # 'apple-banana-cherry' it joins the list into a string with '-' in between each element
print(new_text)

# Split lines
multiline = "Line1\nLine2\nLine3"     # string with new line characters and it creates three lines
lines = multiline.splitlines() # ['Line1', 'Line2', 'Line3']
print(lines) # it splits the string into a list wherever there is a new line character



# 6. Replace & Translation

blog = "I like cats and cats are cute"

# Replace substring
new_text = blog.replace('cats', 'dogs') 
print(new_text) # "I like dogs and dogs are cute"

# Remove specific characters
text2 = "Hello! World?"
clean = text2.replace('!', '').replace('?', '') # remove '!' and '?'with empty space
print(clean) # "Hello World"


# 7. Prefix/Suffix Checks
filename = "document.pdf"
url = "https://example.com"

print(filename.startswith('doc'))    # True because 'document.pdf' starts with 'doc'
print(filename.endswith('.pdf'))     # True because 'document.pdf' ends with '.pdf'
print(url.startswith('https'))       # True because 'https://example.com' starts with 'https'
print(url.endswith('.com'))          # True because 'https://example.com' ends with '.com'