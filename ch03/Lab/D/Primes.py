"""
Primes.py
Given an integer input n, this program (for Lab 3D) lists which 
numbers from 1 to n are prime and furthermore shows
a factorization for any composite numbers.
@author Jake Gadaleta
"""

#ASK THE USER FOR AN INTEGER - CALL IT n
n = int(input('Gimme a number: '))
#FOR EACH INTEGER FROM 2-n:
for i in range(2,n):
	#Loop over the integers less than n and see if any 
	#divide n.  As soon as one does, print n as a product 
	#(so as to prove n is not prime) and then break out of the
	#loop.
	if 	n % i == 0:
		print(f'{n} is divisable by {i} and {int(n/i)}')
		break
	#In the else loop of the loop (which would only be 
	#called if we did NOT break out of the loop, meaning that
	#n i
	# 
	# 
	# .s indeed prime)  print that x must be prime.  
else:
	print(f'{n} is Prime')

