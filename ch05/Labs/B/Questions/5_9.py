"""
5.9 (PALINDROME TESTER) 
A string that’s spelled identically backward and forward, like 'radar', is a palindrome. 
Write a function is_palindrome that takes a string and returns True if it’s a palindrome and False otherwise. 
Use a stack (simulated with a list as we did in Section 5.11) to help determine whether a string is a palindrome. 
Your function should ignore case sensitivity (that is, 'a' and 'A' are the same), spaces and punctuation.
"""

def palidrome(stringy):
    og = stringy.lower()
    flipped = stringy.lower()[::-1]
 
    return og == flipped
if __name__ == "__main__":
    print(f"""
    Jake:  {palidrome("Jake")}
    RaDaR: {palidrome("RaDaR")}
    """)