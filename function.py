# if i know how many arguments i will pass to a function
def my_func(fname,lname):
    print(fname + " " + lname)

my_func('ahmed','masum')

# if i don't know how many arguments i will pass to a function

def my_func(*name):
    print("welcome to " +name[1])
    print('welcome to ' + name[2])

my_func('ahmed','masum','ali')


# agrument sent key = value syntex

def myfunction(c1,c2,c3,c4):
    print('the youngest child is'+ " " + c1,c2,c3,c4)
myfunction(c1='Email',c2 ='Alba',c3 = 'Syra',c4 = 'emyra')



# if the number of keyword arguments are unknown, add a double ** before the parameter name:


def myfunction(**name):
    print ("his first name is " + name['fnam'], 'his last name is ' + name['lnam'] , 'his email is ' + name['email'])
myfunction(fnam='John',lnam='Doe',email='johndoe@example.com')



# default parameter value
def myfunc(country = "Bangladesh"):
    print('I am from:' + country)
myfunc()



# passing a agrument

def myfunc(fruits):
    for x in fruits:
        print(x)
fruits = ['apple','banana', 'cherry','banana']
myfunc([fruits])