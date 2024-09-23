# floor division
# arithmetical operators
#  +-/....
x = 15
y = 2
print(x//y) # type: ignore

# exponential

print(x**y)

# assainment operators
x += 3
x=18
print(x) # x = x+3
x /=3  #  x = x / 3
print(x)

# comparison operators
# comparison operators  are used to comapare operators two values
print(x > y) # True
print(x < y) # False
print(x == y) # False
print(x!= y) # True

# logical operators


# logical operators are used to combine conditional statements
print(x > y and x < 10) # True
print(x > y or x < 10) # True
print(not(x > y)) # False


# python identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True
print( x is not y) # true



# python membership operators are used to test if a sequence is presented in an object:

x = ["apple", "banana"]
print("banana" in x) # True
print("cherry" in x) # False
print('cherry' not in x) #true

# bitwise opertor is used to test if a sequence is presented in an object:
