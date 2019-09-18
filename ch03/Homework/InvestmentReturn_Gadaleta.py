'''
InverstmentReturn_Gadaleta
Completes what is listed in 3.10
Jake Gadaleta

2.12 (7% INVESTMENT RETURN) 
Some investment advisors say that it’s reasonable to expect a 7% 
return over the long term in the stock market. 
Assuming that you begin with $1000 and leave your money invested, 
calculate and display how much money you’ll have after 10, 20 and 30 years. 
Use the following formula for determining these amounts:

a = p(1 + r)^n

where

p is the original amount invested (i.e., the principal of $1000),

r is the annual rate of return (7%),

n is the number of years (10, 20 or 30) and

a is the amount on deposit at the end of the

nth year.

3.10 (7% Investment Return) Reimplement Exercise 2.12 
to use a loop that calculates and displays the amount of money you’ll have each year at the ends of years 1 through 30.
'''

r = 1.07
n = 0
p = 1000

while n <= 30:
    a = round(p * (r ** n), 2)
    print('Year', n, '\n\tAmount', a, sep=': ')
    n += 1