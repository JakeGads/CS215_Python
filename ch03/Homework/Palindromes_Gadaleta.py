"""
3.12 (Palindromes) A palindrome is a number, word or text phrase 
that reads the same backwards or forwards. 
For example, each of the following five-digit integers is a 
palindrome: 12321, 55555, 45554 and 11611. 
Write a script that reads in a five-digit integer and determines whether it’s a palindrome. 
[Hint: Use the // and % operators to separate the number into its digits.]


"""
user_string = input("Gimme a number\t") # take the user number as a string
user_reverse = '' # use this to reverse the string for easy comparison

n = len(user_string) # find the length so we can analyze it in a loop
counter = 0

user_number = int(user_string) # the number that we will use to do all of the mathematics

while counter < n:
    temp = user_number % 10 # find the rightmost number
    user_number //= 10 # pop the rightmost number off

    user_reverse += str(temp) # append the number to generate a reverse
    counter += 1 # add to the counter

if user_string == user_reverse: # this is if they are the same thing
    print(user_string, 'is a palidrome')
else: # this is if they are not the same thing
    print(user_string, 'is not the same as', user_reverse)