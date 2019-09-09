"""
Lab3B_IfAndWhile.py

This program practices if statements (if-else, if-elif, if-elif-else) and 
while loops while validating input and looking for patterns.

Jake Gadaleta
"""

############################################################################
#Task 1 
############################################################################

#Input Validation Program

x = int(input("Enter 1 or 2 please: "))
counter = 1

while x!=1 and x!=2:  #check to see if x is neither 1 nor 2.
    x = int(input("Enter 1 or 2 please: ")) #Re-ask for a 1 or 2.
    counter += 1
    
print("\nFINALLY! It took you {counter} times - geesh!".format(counter=counter) )


############################################################################
#Task 1 Continued - Ask the user for an even integer
############################################################################
x = int(input("Please enter an even number:\t"))
counter = 1
while not (x % 2 == 0):
    x = int(input("I SAID INPUT AN EVEN NUMBER:\T"))
    counter += 1

print('FINALLY! It took you {counter} times to remember what an even number is'.format(counter=counter))

############################################################################
#Task 2 - Using the counter to do math
############################################################################

#Ask the user for how many rows.
numRows = int(input("Enter an how many rows you'd like to see: "))

#Set the counter to a starting value.
counter = 0

# print the header
print("number\tsquare\tcube") 


#Use a loop to print out the rest of the rows.
while (counter < numRows):
    print(counter,'\t',counter ** 2,'\t', counter ** 3)
    counter += 1



############################################################################
#Task 3 - Using the coutner to do math
############################################################################


#Get input
x = input("Input an integer: ")

#The len(string) function returns the length of a string
#Look at your lab handout!  I want you to type it to remember it.
n = len(x)

counter = 0

#HINT:  A line of code goes here.  What type of variable is x?
x = int(x)
while counter < n:
    counter += 1
    temp = x // (10**(n-counter))
    x %= (10**(n-counter))

    print(temp, sep='', end='     ')
print()
#Do the expected truncation/remainder logic to get the leftmost digit.
#print the leftmost digit
#update the counter as needed.

    
############################################################################
#Task 4 - Age Classification
############################################################################

age = int(input("How old are you?\t"))

if age <= 1:
    print("You are an infant")
elif age > 1 and age < 13:
    print("You are a child")
elif age >= 13 and age < 20:
    print('You are a teenager')
else:
    print("You are an adult")