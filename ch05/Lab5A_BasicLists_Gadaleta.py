"""
Lab5A_BasicLists_Gadaleta.py
Completed the sepcifications of the lab
Author: Jake Gadaleta
"""

def num_letters(words):
    """Pareses the words as a enumerates"""
    for i,h in enumerate(words):
        print(i,":\t",h)

def parityCheck(values):
    """checks the oddness or evenness of a list of numbers"""
    returner = []
    for i in values:
        if i % 2 == 0:
            returner.append("odd")
        else:
            returner.append("even")

    return returner



if __name__ == "__main__":
    num_letters(["Please", "exucse", "my", "dear", "aunt", "sally"])
    print("\n\n")
    num_letters("Justin likes penut butter")
    print("\n\n")
    num_letters(["Justin", "likes", "penut", "butter"])
    print("\n\n")
    print(parityCheck([0,10,12,14,15,7,9,11]))
    print(parityCheck([0,11,15,11,25,97,9999,11]))




