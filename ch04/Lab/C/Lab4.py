"""
Lab4.py
Follows the examples laid out in the Lab4C Doc
author: Jake Gadaleta
"""
import statistics

"Functions"
def average(*args):
    """Finds the average of an arbitrary number of values"""
    return (sum(args)/len(args))

def product(*args):
    """Calculates the average of a list or tuple"""
    product = 1
    for i in args:
        product *= i
    
    return product

def getNames():
    """Requests a first and last name and returns it."""
    first = input("What is your first name? ")
    middle = input("What is your middle name")
    last = input("What is your last name? ")
    return (first, middle, last)

def getMyStats(*args):
    return (
        min(*args),
        max(*args),
        statistics.mean(*args),
        statistics.median(*args)
    )






x = 10
tuple1 = (2, "hi", x)
tuple2 = (3.14, 5**2, 10, 11, 12)

print(tuple1)
print(tuple2)


print(*tuple1)
print(*tuple2)

yList = [1,5,4,1,2,6]
yTuple = (1,5,4,1,2,6)

print(yList)
print(yTuple)

print(*yList)
print(*yTuple)

print(yList == yTuple)

print(average(5,8,14))
print(average(-1,4,5,-8))
average(2,10)

print(average(*yTuple))

print(average(*yList))

print(product(2,4,6))
print(product(-1,-1,-1,-3))


# fullName = getNames()
# print(fullName)
# print("First:", fullName[0])
# print("Middle:", fullName[1])
# print("Last:", fullName[2])

stats = getMyStats((98,97,55,82,73,88))
print(stats)
print(
    f'''
    Min: {stats[0]}
    Max: {stats[1]}
    Mean: {stats[2]}
    Median: {stats[3]}
    '''
)