# -*- coding: utf-8 -*-
"""
FunctionsWithDefaultAndNone.py 
Lab Ch 4B: In this file we learn how to use default parameter values and 
we learn more about returning None. 
@author: Jake Gadaleta
"""

def rectangleArea(width, length = 10):
    """Calculates the area of the retangle"""
    return length* width

def sillyFunction(x = -1):
    '''This function is NONEsense.'''
    if 1<x<9:
        return x**2
    elif x >= 9:
        return x**0.5
    

if __name__ == "__main__":
    y = sillyFunction(3)
    print (f"output when 3 is passed in: {y}")

    y = sillyFunction(9)
    print (f"output when 9 is passed in: {y}")

    y = sillyFunction(16)
    print (f"output when 16 is passed in: {y}")

    y = sillyFunction(-1)
    print (f"output when -1 is passed in: {y}")


    #Ask the user for input
    #userInput = int(input("Enter a number for silly Function: "))
    #y = sillyFunction(int(input("Give me a number: ")))
    y = sillyFunction(-1)
    
    if y:
        print("Silly Function returned Something meaningful")
    else:
        print("Silly Function Returned None")

    print(f"output when nothing is passed in: {sillyFunction()}")

    print(rectangleArea(2,3))
    print(rectangleArea(2))


