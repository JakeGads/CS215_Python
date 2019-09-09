"""
3.21 (Calculate Change Using Fewest Number of Coins) 
Write a script that inputs a purchase price of a dollar or less for an item. Assume the purchaser pays with a dollar bill. 
Determine the amount of change the cashier should give back to the purchaser. 
Display the change using the fewest number of pennies, nickels, dimes and quarters. 
For example, if the purchaser is due 73 cents in change, the script would output:


Your change is:
2 quarters
2 dimes
3 pennies
"""

totalAmount = int(input('Enter an amount of Cents\t')) # Holds the amount of less then one dollor change

# zeros everything out to avoid a name error on the report
quarters = 0
dimes = 0
nickles = 0
pennies = 0

# my absoulute fav: input validation
while(totalAmount > 100):
    print('Cannot handle more than one dollor')
    totalAmount = int(input('Enter an amount of Cents\t'))

# checks if there is more than 1 quater
# this process is repeated for every coin
if totalAmount >= 25:
    quarters = totalAmount // 25 # if there is see how many quaters can be assigned
    totalAmount = totalAmount - (25 * quarters) # subtract my amount of quaters from the total

if totalAmount >= 10: # checks to see if there is a dime or more 
    dimes = totalAmount // 10
    totalAmount = totalAmount - (10 * dimes)

if totalAmount >= 5:
    nickles = totalAmount // 5
    totalAmount = totalAmount - (5 * nickles)

if totalAmount >= 1:
    pennies = totalAmount // 1
    totalAmount = totalAmount - pennies

# Report Statment
print(
    """
    {quarters} quarters
    {dimes} dimes
    {nickles} nickles
    {pennies} pennies
    """.format(
        quarters = quarters,
        dimes = dimes,
        nickles = nickles,
        pennies = pennies
    )
)