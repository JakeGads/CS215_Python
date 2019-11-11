"""
Write a function called getCorrectInput1.  
The function should ask the user for a number between 1 and 10 over using input validation.  
The function should return user input in the correct range. 
"""


def getCorrectInput1():
    user = input("Enter a value between 1 and 10")
    while user >= 1 and user <= 10:
        user = input("Enter a value between 1 and 10")
    return user


"""
Write a function called getCorrectInputV2 that takes in a starting point and ending point.  
The function should ask the user for a number between this starting point and ending point and should perform input validation on the user's input.  
The function should return user input in the correct range, that is, between the starting and ending point.   
The function should default to a starting point of 1 and an ending point of 10 if no parameters are passed.  
(HINT:  COPY AND PASTE getCorrectInput1 and update it as needed.)
"""


def getCorrectInput1(low, high):
    user = input("Enter a value between 1 and 10")
    while user >= low and user <= high:
        user = input("Enter a value between 1 and 10")
    return user


"""
    3. Write a function typeOfMember that takes in a total amount of purchases that a customer has made at a store.  
    The function should return:

"GOLD"  if the person has spent at least $1000 
"SILVER"  if the person has spent $500-$1000 
"STANDARD"  if the person has spent $250-$500
Nothing otherwise.

Test the nothing case as such:  If a customer is deemed to not have a membership, the customer is told how much more they have to spend to get a standard membership.  
Do this by making use what is returned in the final case above.  Remember:  Every function will return a value even if you don’t ask it too.  What is that value?
"""
def typeOfMember(paid):
    if paid > 1000:
        return "GOLD"
    elif paid > 500:
        return "SILVER"
    elif paid > 250:
        return "STANDARD"
    
"""
4. Write a function tallyWordsArb that accepts an arbitrary number of words and prints a table tallying how many times each word occurs.  
Test your code with these input 
TEST 1 (call your function with an arbitrary listing): 
turkey, cranberry, stuffing, stuffing, pie, turkey, turkey, turkey, gobble

TEST 2 (call your function an actual list object):  
[turkey, cranberry, stuffing, stuffing, pie, turkey, turkey, turkey, gobble]

"""

def totalWordsArb(*args):
    if not isinstance(args[0], list):
        words = list(args)
    else:
        words = args[0]
   
    words.sort()
    i = 0
    while i < len(words):
        print(f"{words[i]}: {words.count(words[i])}")
        i -=- words.count(words[i])

    print()
    
totalWordsArb("turkey", "cranberry", "stuffing", "stuffing", "pie", "turkey", "turkey", "turkey", "gobble")
totalWordsArb(["turkey", "cranberry", "stuffing", "stuffing", "pie", "turkey", "turkey", "turkey", "gobble"])

"""
5. Write a function tallyWordsList that accepts a SINGLE list of words and prints a table tallying how many times each word occurs.  (HINT: Start with a copy and paste of version 1) Test your code with the input of these words: turkey, cranberry, stuffing, stuffing, pie, turkey, turkey, turkey, gobble. 

TEST 1:  Test your code with an arbitrary list object:  
[turkey, cranberry, stuffing, stuffing, pie, turkey, turkey, turkey, gobble]
TEST 2: Test your code by asking the user to enter a new word or -1 when done entering words.
"""

def tallyWordsList(words):
    words.sort()
    i = 0
    while i < len(words):
        print(f"{words[i]}: {words.count(words[i])}")
        i -=- words.count(words[i])

"""
6. Write a function isFib that determines whether a number is in the Fibonacci sequence, 
and if it is, what it's position is (or -1 if it is not in the sequence).  
The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, etc.

Example: 
isFib(3) returns 4.  
isFib(21) returns 8.  
isFib(9) returns -1.
"""


def isFib(number):
    first = 1
    second = 1
    count = 2
    while number > second:
        count += 1
        if number == first + second:
            return count
        
        temp = second
        second = first + second
        first = temp


    return -1
print(f"""
isFib(3): {isFib(3)}
isFib(21): {isFib(21)}
isFib(9): {isFib(9)}
""")

"""
7. Write a function isFibSubSequence that determines whether an arbitrary sequence of integers is in the Fibonnaci sequence (1, 1, 2, 3, 5, 8, 13, 21, 34, etc):

Example: 
isFibSequence(3, 5, 8) returns true.  
isFibSequence(3, 5, 8, 16) returns false.  
isFibSequence(9, 11, 20, 31) returns false as well.

HINT:  Use isFib to help.  (Challenge for the more experienced:  Try to save processing power by only calling isFib on the first two numbers.)
"""
def isFibSequence(*args):
    if isFib(args[0]) == -1 or isFib(args[1]) == -1:
        return False
    
    count = 2
    while count < len(args):
        if args[count - 1] + args[count - 2] != args[count]:
            return False
        count += 1
    return True

print(f"""
isFibSequence(3, 5, 8):         {isFibSequence(3, 5, 8)}
isFibSequence(3, 5, 8, 16):     {isFibSequence(3, 5, 8, 16)}
isFibSequence(9, 11, 20, 31):   {isFibSequence(9, 11, 20, 31)}
""")