"""
2.10 (ARITHMETIC, SMALLEST AND LARGEST) 
Write a script that inputs three integers from the user. Display the sum, average, product, 
smallest and largest of the numbers. Note that each of these is a reduction in functional-style programming.
"""

myList = [] # Takes the list and asks the user to enter
myList.append(int(input("Enter #{}\t".format(len(myList) + 1))))
myList.append(int(input("Enter #{}\t".format(len(myList) + 1))))
myList.append(int(input("Enter #{}\t".format(len(myList) + 1))))


# takes the max and min
print(
    """
    Max:\t{Max}\n
    Min:\t{Min}
    """.format(
        Max = max(myList),
        Min = min(myList)
    )
)