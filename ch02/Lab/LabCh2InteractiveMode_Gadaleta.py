# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 2
x = 2
y=3

print ('x =', x)
print('Value of', x , '+', x, 'is', (x+x))
print('x = ')
print((x+y), '=', (y+x))

# 3
print ("We\n\thave\n\t\toff\n\t\t\tMonday!\n\t\t\t\tYay!")

x = "C:\\\\MyFolder\\MySubfolder"
print (x)

x = "Mary O'Bono screamed, \"Run spot! Run!!\" and then started running as well"
print(x)

#4
rating = input('Enter an integer rating between 1 and 10: ')
print(type(rating))
print(type(int(rating)))

#5
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)

print(27.5 ** 1/2)
print(27.5 ** (1/2))

#6
x = 7
if x >= 5:
    print (x, 'is at least 5!')
    print ('The square of', x, 'must therefore be at least 25!')

x= 3
if x >= 5:
    print (x, 'is at least 5!')
print ('The square of', x, 'must therefore be at least 25!')

grade = 91
if grade >= 90:
    print('Your Grade of {grade} earns you an A in this corse'.format(grade=grade))

#7
if 1024 % 4 == 0:
    print('1024 is a multiple of 4')

if 17 % 10 == 0:
    print('17 is a multiple of 10')