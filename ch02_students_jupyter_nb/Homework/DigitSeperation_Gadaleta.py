"""
2.11 (SEPARATING THE DIGITS IN AN INTEGER) 
Write a script that inputs a five-digit integer from the user. 
Separate the number into its individual digits. Print them separated by three spaces each. 
For example, if the user types in the number 42339, the script should print
"""
# will and I took like a half to shave off extra lines we thing this is as short as we can get
user = input("Gimme a number\t") # Take the number but leave it as a string
result = '' #stores the result
for i in range(0,len(user)): 
    result += "{}\t".format(user[i]) #pulls out each individual aspect 
print("Result : ", result)
