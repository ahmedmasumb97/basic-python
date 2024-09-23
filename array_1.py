
car = ['ford','volvo','bmw','audit']

# access array

x =  car[0]
print(x)

# modify array

car[1]='mycar'
print(car)


# looping 

for x in car:
    print(x)
    
# adding element in array

car.append('toytota')
print(car)


# removing array element

car.remove('audit')
print(car)

car.pop(2)
print(car)

x = car.count('audit')
print(x)

car.sort()
print(car)