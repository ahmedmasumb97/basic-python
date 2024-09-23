# list of conditions and the following disclaimer
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:
fruits = ['apple', 'orange', 'banana', 'mango']
print(fruits) # ['apple', 'orange', 'banana', 'mango']
print(len(fruits)) # ['apple', 'orange', 'banana',



# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Using the list() constructor to make a List:


numbers = list((1, 2, 3, 4, 5))
print(numbers) # [1, 2, 3, 4, 5]

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[2:4])
print(thislist[2:])
thislist.insert(2,'mango')
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.append('berry')
print(thislist)
thislist.append([1, 2, 3,])
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.append(tropical)
print(thislist)

f1 = ['apple', 'banana', 'cherry']
f2 = ['kiwi', 'orange', 'melon']
f1.extend(f2)
print(f1)

f1.remove('apple')
print(f1)
f2.pop(1)
print(f2)
f2.pop()
print(f2)


thislist = ["apple", "banana", "cherry"]
del thislist[1]
print(thislist)
del thislist
# print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

fruits = ['apple', 'banana', 'cherry','cherry','orange']
for x in fruits:
    print(x)


for x in range(len(fruits)):
    print(fruits[x])


for x in range(1,10):
    print(x)
    
    
# list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)


# The Syntax
# newlist = [expression for item in iterable if condition == True]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [  x for x in fruits if 'a' in x]
print(newlist)

newlist = [x for x in fruits if x  != 'apple']
print(newlist)

newlist = [x for x in fruits]
print(newlist)


newlist = [ x for x in range(10)]
print(newlist)

newlist = [x  for x in range(1,10,2)]
print(newlist)

newlist = [x for x in range(2,10,2)]
print(newlist)


newlist = [x for x in range(10) if x % 2 == 0]
print(newlist)
newlist = [x for x in range(100) if x%5 == 0]
print(newlist)

newlist = [x for x in range(100) if x%3==0 and x%5==0]
print(newlist)

list = [1,4,5,10,3,15,20,18,14,10]
newlist = [x for x in list if x> 5]
print(newlist)
newlist = ['even' for x in list if x%2==0] 
print(newlist)

fruits = ['apple', 'range', 'Multa', 'orange']
newlist = [x if x != 'multa' else 'banana' for x in fruits]
print(newlist)

fruits.sort(key = str.lower)
print(fruits)

fruits.reverse()
print(fruits)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.append(list2)
print(list1)

for x in list1:
    list2.append(x)
print(list2)

# turples

mytuple = ('apple', 'orange', 'banana', 'orange')



# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# tuples,order is important and tuples is unchangeabel which means when a created a tuple it does not to allow to chanage it's item,delete or add any item into tuples but duplicates is allow



# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

fruits = tuple(('apple', 'orange','banana'))

#  in tuples any element can not update but is is possible to alternative way
# x = ('apple', 'orange','banana','multa')
# y = list(x)
# y[2] = "cherry"
# x = tuple(y)
# print(x)


# Python - Unpack Tuples


fruits = ('apple','orange','banana','orange')
(apple,orange,banana,orange) = fruits
print(apple)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,*blue) = fruits
print(green)
print(blue)

# in python have 4 types collection data type ,every data are used for differnt purposes
# in set data type , it is unchangeable which it can not change but it's order is not important but whears tuples order is important

# A set is a collection which is unordered, unchangeable*, and unindexed and duplicates values are not allow

fruits = {'apple','manago','lemon'}
print('lemon' in fruits)
print('melon' not in fruits)
print('lemon' is not fruits)
# fruits.pop('apple')


fruits = {'apple', 'banana', 'cherry'}
fruits.add('orange')
fruits.add('guava')
print(fruits)
f1 = {'apple','lemon'}
fruits.update(f1)
print(fruits)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

fruits = ['apple', 'banana', 'cherry']
# fruits.remove('banana1')
# do not use remove for deleting element from the set use distinct()


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
# or set3 = set1 | set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# dict

cars = {
    'brand':'ford',
    'Model':'Mustang',
    'Year': 1964
}

print(cars['brand'])
print(cars.get('Model'))

# dict : orderd and changeable,duplicates not supported


# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
key = thisdict.keys()
value = thisdict.values()
print(key,value)

for [key,value] in thisdict.items():
    print(key,value)