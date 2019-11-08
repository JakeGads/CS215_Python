"""
LabD_ComplexLists_Gadaleta.py
An overview of list comprehesions, lamndas, map() and function
author Jake Gadaleta
"""
#@Dr. Ryan all just exist in the main for tutoring purposes, as does the spread out notation you see

students = [("Karen", "Sophomore"), ("Pranshu", "Junior"), ("Ann", "Senior"),
                       ("Carl", "Freshmen"), ("Cait", "Freshmen"), ("Kathleen", "Sophomore")]

upperClassmen = [student[0] # takes only the first part
    for student in students # checks every student
    if student[1] != "Freshmen"] # returns the student if he/she is not a freshman

print(upperClassmen) # display


print(
    sum(
        map( # takes all values of the second argument and
            lambda x: x*3, # mults 3
            filter ( # allows for the filtering of the list, THIS ENTIRE THING IS THE SECOND ARGUMENT
                lambda x: x % 2 == 0, # checks if the value is even
                range(1,11) # the orginal list
                )))) 


# notice this flips the map and filter what is the outcome of this
print(
    sum([
        number * 3 
        for number in range(1, 11) 
        if number % 2 ==0 
        ]))

numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
l = list(
    map(
        lambda x: x * 2,
        filter(
            lambda x: x % 2 == 0, 
            numbers
        )))
print (l)

l = list(
    filter(
        lambda x: x % 2 == 0,
        map(
            lambda x: x * 2, 
            numbers
    )))
print(l)