"""
testCorrection_Gadaleta.py
implements a function for the quadratic formula
author: Jake Gadaleta
"""

def quadratic(a,b,c):
    des = (b**2) - (4*a*c)

    if des < 0:
        return "No real soultions"
    elif des == 0:
        return f"One soultion {(-b) / (2*a)}"
    else:
        des = des ** .5
        return f"Two soultions {(-b + des) / (2 * a):.2f} and {(-b - des) / (2 * a):.2f}"

print(quadratic(1,-1, -6))
print(quadratic(1, -6, 9))
print(quadratic(2,1,1))