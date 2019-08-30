"""
2.10 (ARITHMETIC, SMALLEST AND LARGEST) 
Write a script that inputs three integers from the user. Display the sum, average, product, 
smallest and largest of the numbers. Note that each of these is a reduction in functional-style programming.
"""

listicle = []
listicle.append(int(input("Enter #{}\t".format(len(listicle) + 1))))
listicle.append(int(input("Enter #{}\t".format(len(listicle) + 1))))
listicle.append(int(input("Enter #{}\t".format(len(listicle) + 1))))

print(
    """
    Max:\t{Max}\n
    Min:\t{Min}
    """.format(
        Max = max(listicle),
        Min = min(listicle)
    )
)