"""
DescriptiveStatsManyInts_Gadaleta

This file contains the code for question 3.8 with edits from dr ryan

@author Jake Gadaleta
"""

"""
3.8 (Arithmetic, Smallest and Largest) In Exercise 2.10, you wrote a script that input three integers, then displayed the 
sum, average, product, 
smallest and largest of those values. 
Reimplement your script with a loop that inputs four integers.

Read #3.8. However, instead of asking the user to input 4 integers, let them input as many as they wish.  Use the letter 
"z" as a sentinel, meaning, when they enter the letter "z", we know they are done inputting integers.

Name your file DescriptiveStatsManyInts_YourName.py.

Of course, points will be taken off if the usual conventions are not followed.

"""
# take the input
temp = input('Give me #1\t')

# if its the sentinal force an exit
if temp == 'z':
    exit()

# Does the intial count
temp = int(temp)
counter = 1
mySum = temp
average = temp / counter
product = temp
smallest = temp
largest = temp

while temp != 'z':
    # add to the counter
    counter += 1
    # recive next import
    temp = input('Give me #{counter} or enter \'z\' to exit\t'.format(counter=counter))

    # check if the sential was called and if it is leave it behind
    if temp == 'z':
        break

    # cast to int
    temp = int(temp)

    # do all of my calculations and checks the largest and smallest
    mySum += temp
    average = mySum/counter
    product*=temp

    if temp > largest:
        largest = temp
    
    if temp < smallest:
        smallest = temp


# Report Statments
print(
    """
    Counter:\t{counter} 
    Sum:\t{mySum}
    Average:\t{average}
    Product:\t{product}
    Largest:\t{largest}
    Smallest:\t{smallest}
    """.format(
        counter = counter,
        mySum = mySum,
        average = average,
        product = product,
        largest = largest,
        smallest = smallest,
    )
)