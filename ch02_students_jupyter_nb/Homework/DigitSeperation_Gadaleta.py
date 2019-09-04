"""
2.11 (SEPARATING THE DIGITS IN AN INTEGER) 
Write a script that inputs a five-digit integer from the user. 
Separate the number into its individual digits. Print them separated by three spaces each. 
For example, if the user types in the number 42339, the script should print
"""
# will and I took like a half to shave off extra lines we thing this is as short as we can get
user = int(input("Gimme a 5 Digit number\t")) # Take the number but leave it as a string

one = user % 10 # gets the 1st character
user //= 10 # removes that character

two = user % 10
user //= 10

three = user % 10
user //= 10

four = user % 10
user //= 10

five = user % 10
user //= 10

print (five, '\t', four, '\t', three, '\t', two, '\t', one)
# I really wish that I could have used lists 