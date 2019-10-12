"""
FunctionPractice_Gadaleta.py
2 functions,
 A) circleGeometry - takes a radius and returns the area and the circumference
 B) Letter Multi, takes in a letter with a conjoining number to print that character that many times
author: Jake Gadaleta
"""
from math import pi


def circle_geometry(radius):
    return (
        pi * (radius ** 2), # area
        2 * pi * radius #circumference
    )

def letter_multiplier(args):
    if len(args) % 2 is not 0:
        return "There is an improper amount of variables in the tuple"

    returner = ''
    for i in range(0, len(args), 2):
        returner += args[i] * args[i+1]

    return returner

for i in range(30):
    temp = circle_geometry(i)
    print(
    f"""
    Rad:\t\t{i:<15.2f} units
    Area:\t\t{temp[0]:<15.2f} units
    Circumference:\t{temp[1]:<15.2f} units
    """
    )

x = "L", 4, "H", 8
print(letter_multiplier(x))
x = "L", 4, "p", 3, "j", 2
print(letter_multiplier(x))