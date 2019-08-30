"""
2.11 (SEPARATING THE DIGITS IN AN INTEGER) 
Write a script that inputs a five-digit integer from the user. 
Separate the number into its individual digits. Print them separated by three spaces each. 
For example, if the user types in the number 42339, the script should print
"""

user = input("Gimme a number\t")
result = ''
for i in range(0,len(user)): result += "{}\t".format(user[i])
print("Result : ", result)