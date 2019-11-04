def five_five():
    """
    5.5 (IPYTHON SESSION: SLICING) Create a string called alphabet 
    containing 'abcdefghijklmnopqrstuvwxyz', 
    then perform the following separate slice operations to obtain:
    """
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

    alpha = 'abcdefghijklmnopqrstuvwxyz'


    print(f"""
    {q1()}
    {q2()}
    {q3()}
    {q4()}
    {q5()}
    {q6()}
    {q7()}
    """)

def five_seven():
    """
    5.7 (DUPLICATE ELIMINATION) Create a function that receives a list and returns a (possibly shorter) 
    list containing only the unique values in sorted order. 
    Test your function with a list of numbers and a list of strings.
    """

    def remove(data): 
        """An implementation of duplicate remover using [not in]"""
        final_list = [] 
        for num in data: 
            if num not in final_list: 
                final_list += [num] 
        return final_list 

    def remove2(data):
        """An implementation of duplicate remover using [set]"""
        return set(data)

    def remove3(data):
        """An implementation of duplicate remover using ["classical"(another word for non-pythonic) for loop]"""
        data.sort()

        i = 0
        while True:
            if data[i] == data[i+ 1]:
                del data[i]
                i-=1
            i+=1

            if i == len(data) - 1:
                return data



        

    print(remove3([1,1,1,1,1]))
    print(remove3(["Jake", "Ryan", "Jake", "Ryan", "Micker", "Micker", "Ryan", "Ryan", "Ryan", "Ryan", "Ryan", "Brian", "Thomas", "Maggie", "Chris", "Mark", "Paul"]))

def five_nine():
    """
    (Palindrome Tester – Now with lists!) A string that’s spelled identically backward and forward, like
    'radar', is a palindrome. Write a function isPalindrome that takes a string and returns True if it’s a
    palindrome and False otherwise. Your function should ignore case sensitivity (that is, 'a' and 'A' are
    the same), spaces and punctuation.
    """
    def isPalindrome(stringy):
        special_chars = " \"',.?\\/|[]{}()|!@#$%^&*-_=+<>\n\t\r\b\f\v\0"
        for i in special_chars:
            stringy.replace(i, "")
        og = stringy.lower()
        flipped = stringy.lower()[::-1]
    
        return og == flipped

    print(f"""
    Jake:  {isPalindrome("Jake")}
    RaDaR: {isPalindrome("RaDaR")}
    """)

if __name__ == "__main__":
    five_five()
    five_seven()
    five_nine()