'''
Factorial_Gadaleta
Does what is outlined in 3.13
Jake Gadaleta

3.13 (Factorials) 
Factorial calculations are common in probability. 
The factorial of a nonnegative integer n is written n! (pronounced “n factorial”) and is defined as follows:

n! = n · (n - 1) · (n - 2) · … · 1

for values of n greater than or equal to 1, with 0! defined to be 1. So,

5! = 5 · 4 · 3 · 2 · 1

which is 120. 
Factorials increase in size very rapidly. 
Write a script that inputs a nonnegative integer and computes and displays its factorial. 
Try your script on the integers 10, 20, 30 and even larger values. 
Did you find any integer input for which Python could not produce an integer factorial value?
'''
user_number = int(input("Gimme a number and I'll do a factorial of it\t"))

while user_number <= 0:
    print('Number must be 1 or higher')
    user_number = int(input("Gimme a number and I'll do a factorial of it"))

print(user_number, 'factorial is', end=' ')

product = 1
while user_number > 0:
    product *= user_number
    user_number -= 1

print(product)