# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 10:38:20 2019

@author: Install
"""

# calculate geometric values of a circle
def circle():
    pi = 3.1415926
    
    radius = float(input("Please enter a raduis: "))
    
    diameter = 2 * radius
    circumference = 2 * pi * radius
    area = pi * (radius ** 2)
    
    print("""
       Here are the calculations for a circle with radius {radius}
           Diameter: {diameter}
           Circumference: {circumference}
           Area: {area}
    """.format(
    radius=radius, 
    diameter=diameter,
    circumference=circumference,
    area = area
    ))
    
#Determine the parity of an integer
def parity():
    x = int(input('Enter an integer: '))
    parity = 'odd'
    if x % 2 == 0:
        parity = 'even'
        
    print('You entered', x, 'which is', parity)

#Create a table of squares and cubes
def squares_and_cubes():
    print("number\tsquare\tcube")
    for i in range(5):
        print("{number}\t{square}\t{cube}".format(number=i,square=i**2, cube=i**3))

if __name__ == "__main__":
    #circle()
    #parity()
    squares_and_cubes()