#boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
    

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#Most Values are True
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
#Some Values are False
#In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean
def myFunction():
    return True

print(myFunction())

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")

#Python also has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))

#Python Operators
#Operators are used to perform operations on variables and values.
#Python divides the operators in the following groups:
#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operator
#Membership operators
#Bitwise operators
#Python Arithmetic Operators
#Operator	Name	Example	Try it
#+	Addition	x + y
#-	Subtraction	x - y
#*	Multiplication	x * y
#/	Division	x / y
#%	Modulus	x % y
#**	Exponentiation	x ** y
#//	Floor division	x // y
#Python Assignment Operators
#Operator	Example	Same As	Try it
