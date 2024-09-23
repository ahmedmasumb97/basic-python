# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops


i=1
while i<10:
    print(i)
    i += 1  
    
# break statements

i = 0
while i <10:
    print(i)
    if i == 5:
        break
    i += 1

print('------------------------------------------------') 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  


fruits = ["apple", "banana", "cherry",'orange', 'multa']
for x in fruits:
    if x == 'apple':
        continue
    print(x)
    
for x in range(2,10,3):
    print(x)
    
    
# nasted loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
size = ['small', 'medium', 'large']

for x in adj:
    for y in fruits:
        for z in size:
            print(x, y, z)