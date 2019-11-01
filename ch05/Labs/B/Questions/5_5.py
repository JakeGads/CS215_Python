"""
5.5 (IPYTHON SESSION: SLICING) Create a string called alphabet 
containing 'abcdefghijklmnopqrstuvwxyz', 
then perform the following separate slice operations to obtain:
"""

alpha = 'abcdefghijklmnopqrstuvwxyz'

def q1():
    """The first half of the string using starting and ending indices."""
    return alpha[0:int(len(alpha)/2) + 1]

def q2():
    """The first half of the string using only the ending index."""
    return alpha[:int(len(alpha)/2) + 1]
def q3():
    """The second half of the string using starting and ending indices."""
    return alpha[int(len(alpha)/2) + 1: 26]

def q4():
    """The second half of the string using only the starting index."""
    return alpha[int(len(alpha)/2) + 1: 26]

def q5():
    """e) Every 5th letter in the string starting with 'c'.."""
    return alpha[2::5]

def q6():
    """f) The entire string in reverse."""
    return alpha[::-1]
def q7():
    """Every third letter of the string in reverse starting with 'z'."""
    return alpha[::-3]


if __name__ == "__main__":
    print(f"""
    {q1()}
    {q2()}
    {q3()}
    {q4()}
    {q5()}
    {q6()}
    {q7()}
    """)