# slicing of string
# string[start:stop:step]

b = "Hello, World!"
print(b[2:5])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# String Length
a = "Hello, World!"
print(len(a))

# String Methods
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))  # returns Jello, World!

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Check String
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
