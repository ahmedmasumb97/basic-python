# a class is like an object constructor or blue prent for creating objects

class Myclass:
    x = 5
    y = 4
    z = x+y


p1 = Myclass()
x = p1.z
print(x)
print(p1)



# in every class have a function which is init function when class is started then this function is executed


class Person:
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location
        
# the str function controls what should be returned when tthe class object is presented as a string
    def __str__(self):
        return f"Hi! I am {self.name}  from {self.location} and my age is {self.age}"
    
    # in a class having a function that is called object method
    
    def method(self,language):
        print (f"hello! I am {self.name} and my language is {language}")
        def myfunc():
            print('======')
            print(self.name)
    
        return myfunc



print(Person)       

p1 = Person('masum',27,'gazipur')
p2 = Person('hasan',27,'Dhaka')
# when create an new object then every time init function is called automatically

print(p1.location)
print(p2.location)
# print p1 object like as string buy using str function
print(p1.__str__())

print('inner function')
x  = p1.method('English grammer')
print(x)


# object method calling

x = p1.method("Bangla")
print(x)

x = p1.method("Bangla")




# here self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# in here self: mysillyobject and abc and which is a reference to the current instance of the class and is used to access variables that belongs to the class.
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()