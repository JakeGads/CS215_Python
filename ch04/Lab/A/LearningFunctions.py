"""
LearningFunctions.py
Lab 4A: writing several basic functions
@author
"""
'Determins a letter grade for any given score'
def findLetterGrade(score):
    if score < 60: # if they score below a 60 they get an F
        return 'F'
    elif  score < 70: # if they score below a 70 but greater then a 60 they get an D
        return 'D'
    elif score < 80: # if they score below a 80 but greater then a 70 they get an C
        return 'C'
    elif score < 90: # if they score below a 90 but greater then a 80 they get an B
        return 'B'
    else: # if they score a 90 or above they get an A
        return 'A'

# calculates how much money was made on the sale of every type of seat
def calculateStadiumSales(a,b,c):
    a_cost = 20 # values for each type of seat
    b_cost = 15
    c_cost = 10

    return (a * a_cost) + (b * b_cost) + (c * c_cost) # returns the sum of the all the individual seats

if __name__ == "__main__":
    # test for findletter grade
    # expect results are A C F
    for i in [95, 75, 52]:
        print('you got a ', findLetterGrade(i), 'when you scored', i)

    # test for calculateStadiumSales
    # expected result is 7015
    print(calculateStadiumSales(72, 155, 325))
    
    a = int(input('A: '))
    b = int(input('B: '))
    c = int(input('C: '))
    print(f'Total Income: ${calculateStadiumSales(a,b,c)}')
