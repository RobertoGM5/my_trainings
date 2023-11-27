# String methods:
""" course = 'Python for beginners'
print(len(course)) """

# Arithmetic Operators
""" print(10//3) # floating division to get an integer as a result
print(10%3) # gives reminder of division """

# Operator precedence
# BODMAS in mathematics

# Math Functions
""" x = 2.9
print(round(x))
print(abs(-2.9)) """

# For loops

""" for item in [1,2,3]:
    print(item,end=' ') """


""" for item in range(5,10,2):
    print(item) """


""" prices =[10,20,30]
total = 0
for price in prices:
    total+=price
print(total) """

# Nested loops
# adding one loop inside of another loop
""" for x in range(4):
    for y in range(3):
        print(f'({x},{y})') """
# challenge
""" numbers = [2,2,2,2,8]    


for x_count in numbers:
    #print('x' * x_count)# easy way to print f with 'x'
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)   """  

## List
# names = ['John','Cena','carry','col']
# print(names[1:])
# write a program to find the largest number in a list
#sol 1
""" lis = [1,50,2,3,8,11,89]
res = max(lis)
print(res)
 """
# sol 2
""" numbers = [1,500,2,3,8,11,89]

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)     """  


## 2D Lists- each item in a list is another list(matrix)
""" matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(row)
    for item in row:
        print(item) """

# write a program to remove duplicates from a list
""" 
numbers = [2,2,4,6,3,4,6,1]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)         """


## Tuples- are immutable
"""Weight converter program"""
weight = int(input('Weight: '))
unit = input('(L) bs or (K) g:')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight/0.45
    print(f"You are {converted} pounds")