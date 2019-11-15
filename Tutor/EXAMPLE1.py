# Taking Input
sayHi = 'Make a user enter the phrase Hello World'

sayHi = input("Please say Hello World")

# Casting
myVar = '69' # Nice, don't touch this
myVarAsAnInteger = 'make this myVar but as an integer'
myVarAsAFloat = 'make this myVar but as a floating point number'

# type()

myVarAsAnInteger = int(myVar)
myVarAsAFloat = myVarAsAnInteger / 1
myVarAsAFloat = float(myVarAsAnInteger)

print(type(myVarAsAnInteger)) # integer int
print(type(myVarAsAFloat)) # float float
print(type('45')) # string str

# // is True division always results in a whole number


# Loops

# write a for loop that prints even numbers between 1 and 25
for x in range (1, 26):
    if x % 2 == 0:
        print(x)

# do the same as above but with step
for x in range(0, 25, 2): # you can only edit this line
    print(x)


# write a while loop that continues to run until the user enters Z ***IMPORTANTE*** count how many times they are in this loop
x = 4
counter = 0
while x != 'z':
    x = input('Gimme a something')

    counter = counter + 1

print("Counter", counter)

# SCARY MATH SHIT

myList = [1,2,3,4,5,6,7,8,9,10,11,11,12,13,14,15] # What is this called
#it is called a list
import statistics
n = len(myList)
numsum = sum(myList)
mean = statistics.mean(myList)
median = statistics.median(myList)
mode = statistics.mode(myList)

# give me the sum, mean, median, mode, 
# of myList

# IF STATMENTS

myInt = 30
# Check if myInt is equal to 30
if myInt == 30:
    print("You did it Bitch! It equals 30!")

# Check if myInt is less than 15
if myInt < 15:
    print("You did it again!")

#Check if myInt is more than 25 if it is check if it is greater than 29 
if myInt > 25:
    if myInt > 29:
        print("It is greater than 29!")
    else:
        print('It\'s greater than 25 but less than 29')

# Calculate the Fibinacci sequence to n = 100
# F(n) = F(n -1) + F(n - 2)
# F(0) = 0
# F(1) = 1
# F(2) = F(1) + F(0) = 1
# F 0, 1, 1, 2, 3, 5,
#  8, 113, 21,34, 51

back2 = 0
back1 = 1
print(back2, '\n', back1)
for i in range(0,100):
    current = back2 + back1
    back2 = back1
    back1 = current
    print(current)


# Recreate this but up to 10
'''
Number  Square  Cube
0       0       0
1       1       1
2       4       8  
'''
print("Number \t Square \t Cube")

for x in range (0, 10):
    square = (x**2)
    cube = (x**3)
    print(f"{x}\t\t{square}\t\t{cube}")
 

# F Stings
myNum = 2.34787
print(
    f'''
    {myNum}
    {myNum:.2f}
    {myNum:.10f}

    {3:<2}i
    {3:>10}i
    '''
)