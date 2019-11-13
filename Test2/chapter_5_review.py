"""
Ask the user for a word and a start/end letter. Return the portion of the word between the first occurrence
of the start letter and the last occurrence of the end letter. Using slicing to get the desired subword.
Recall: what function gives you the position of the FIRST occurrence of an item? (The answer is in the posted
5C notes if you don't know.)
"""


def where(word, start, end):
    word = word.lower()
    start = start.lower()
    end = end.lower()

    startLoc = word.index(start)
    r_word = list(reversed(word))
    endLoc = len(r_word) - r_word.index(end)
    if startLoc < endLoc:
        return word[startLoc:endLoc]
    else:
        return "Not a substring"


print(
    where("jake", "a", "k"),
    where("daniel", "n", "l"),
    where("paul", "u", "p"),
    where("eugene", "e", "e"),
    sep="\n",
)

"""
We can remove duplicates in a list in many ways. Here's two more ways.
Say values = [0, 0, -10, 15, 13, 12, 0, -10, 15, 13, 12, -10, 13, 12]
(a) Create a function removeDuplicates that takes in a list and returns a list containing a new list of only the
unique values. Call the function on the values list above.
def removeDuplicates(myList):
#create an empty list called unique here.
#We'll now add items to unique so that we never add an item twice.
 #Here's some hints how.
for item in myList:
#if the item isn't already in the unique, then put it in there.
(b) We can also use list comprehensions to get a list of unique items. This is more mathematical, but
smooth.
• First go to the posted notes from Ch5A and remind yourself what "enumerate" does and then fill in
the first blank below.
• Finally, fill in the second blank below. HINT: If the number 15 appears at 3 and 8 like in the list
below, then you'd only want to add it to the uniqueList when you analyze it at position 3.
values = [0, 0, -10, 15, 13, 12, 0, -10, 15, 13, 12, -10, 13, 12]
uniqueList = [item for _____________ in enumerate(values) if ___________]
"""


def removeDuplicates(myList):
    new_list = []
    for item in myList:
        if item not in new_list:
            new_list.append(item)

    return new_list


values = [0, 0, -10, 15, 13, 12, 0, -10, 15, 13, 12, -10, 13, 12]

"""
Insert 20 random letters into the range a-f into a list. Perform the following tasks, displaying your results.
(a) Sort the list in ascending order
(b) Sort the list in descending order
(c) Sort the unique values in ascending order
HINT: One way to get random letters from 'abcdef' is to just pick random indices from this string:
 word = 'abcdef'
"""


def sorting_lists():
    alpha = "abcdef"
    from random import randint

    word = ""
    for i in range(20):
        word += alpha[randint(0, len(alpha) - 1)]

    print(sorted(word))
    print(sorted(word, reverse=True))
    word = list(word)
    word.sort()

    i = 0
    while i < len(word):
        count = word.count(word[i])
        del word[word.index(word[i]) + 1 : word.index(word[i]) + count]
        i -= -1
    print(word)


sorting_lists()

"""
Say you have a tuple of students and grades, like below.
[('Ann', 82), ('Mary', 75), ('Terry', 85), ('Clare', 94), ('Kitty', 87), ('Mickey', 77), ('Aggie', 72)]
(a) Use list comprehensions to list the GRADES of everyone who got in the B range (80-89)
(b) Use filter/map to list the NAMES of everyone (in all capital letters) who got in the B range (80-89)
"""

values = [
    ("Ann", 82),
    ("Mary", 75),
    ("Terry", 85),
    ("Clare", 94),
    ("Kitty", 87),
    ("Mickey", 77),
    ("Aggie", 72),
]

comp = [name[0] for name in values if 80 <= name[1] <= 89]
print(comp)

filtered = list(map(lambda x: x[0].upper(), filter(lambda x: 80 <= x[1] <= 89, values)))
print(filtered)

"""
Sum the squares of the odd numbers from 40 to 60 using the following. FYI: The correct answer is 25330.
(a) list comprehensions
(b) generator expressions
(c) filter/maps with lambda expressions 
"""
i = list(range(40, 61))
a = sum([x ** 2 for x in i if x % 2 == 1])
b = sum(x ** 2 for x in i if x % 2 == 1)
c = sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 1, i)))
print(a, b, c, sep="\t")

"""
Given a string of letters, replace every occurrence of a vowel with a capital V. Do this by using
filtering/mapping. 
"""
vowels = 'aeiou'
# TODO return here
word = "jake"

"""
Given a list of numbers (such as our favorite array below), print a list of each value and its frequency. Do
this without removing duplicates. (Hint: just find the min/max of the values.)
"""

dailyChanges = sorted([1, -4, 5, -8, -3, 14, -13, 8, 4, -4, -9, -11, -3, 11, -9, 5,
 -11, 7, 5, -15, 6, 11, -12, -2, 0, -4, 5, 3, 2, 11, 5, -1, 5,
 3, -1, 2, -3, 0, 1, -7, -11, 0, 7, 0, -4, -5, 12, -1, 3, 2,
 -1, -2, 2, -10, -10, 8, 7, -6, -9, -1, 1, 10, -5, 4, 5, 1,
 -10, -3, -2, 5, 1, -4, 1, 1, 3, 9, 6, -1, -8, 5, -27, 10, -1,
 -8, -3, -5, 6, 14, 13, -25, -8, -3, 14, 2, 7, -3, 4, 1, -10,
 4, 7, -5, -7, -1, -2, -7, -5, 3, 16, 8, -2, -14, -2, 7, -4,
 -4, 12, 0, -10, -5, -2, 1, -6, -9, 14, 0, 1, -5, -9, -3, 8,
 -2, 17, -4, -4, 0, -2, -16, 8, 6, -10, -1, 13, 0, -6, 3, 11,
 -14, -6, -3])

i = 0
while i  < len(dailyChanges):
    print(f"{dailyChanges[i]}:\t{dailyChanges.count(dailyChanges[i])}")
    i += dailyChanges.count(dailyChanges[i])

