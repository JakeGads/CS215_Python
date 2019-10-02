'''
Lab_3F_Gadaleta.y
Special Align lab
a: Jake Gadaleta
'''

print(f'''
{1325.43:>7}
{5.17:>7}
{328.48:>7}
''')


print('\n\n')
temperature = 98.6
print(temperature)
print(f'{temperature:.20f}')

from decimal import Decimal

temperature = Decimal('98.6')
print(f'{temperature:.20f}')

x = Decimal('10.5')
y = Decimal('2')

print(x + y)
print(x/y)
x *= y
print(x)


x %= 6
print(x)
print(type(x))

print(x**2)
print(x**2.0)

'''
Align taxes ad what not
'''
r = Decimal('1.05')
p = Decimal('1000')



for i in range(1,11):
    calc = p * (r ** i)
    print(f'{i:<5} ${calc:>2.2f}')