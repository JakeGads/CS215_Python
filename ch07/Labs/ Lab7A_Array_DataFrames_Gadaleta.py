import numpy as np

nums1 = np.array([1,3,5,7,99])
print(nums1)
nums2 = np.array([[1,2,3], [4,5,6]])
print(nums2)

array = np.array([1, 2, 3, 'hi'])
print(array)

# array = np.array([1,2,3], [1,2,3,4])
# print(array)

print(nums2.ndim)
print(nums2.shape)
print(nums2.size)

array = np.arange(1,21)
print(array) #Should see 1-20 in a 1 dimensional list
array = array.reshape(4,5) #This reshapes the list into a 4 by 5 array print(array)
print(array)

array = np.arange(2 * 100_000, 3 * 100_000)
array = array.reshape(100, 1000)
print(array)

#create an array of 4 student’s exam1-exam 3 grades
grades = np.array([
    [87, 96, 70],
    [100, 87, 90],
    [94, 77, 90],
    [100, 81, 82]
])
print(grades)
#Notice that the below code prints the sum/min/etc of ALL the grades
#across all rows and all columns.
print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())

#perform operations ON the columns (x-axis is axis 0)
print("\nstats for cols")
print(grades.sum(axis = 0)) #This gives a 1 by 3 array
print(grades.min(axis = 0))
print(grades.max(axis = 0))
print(grades.mean(axis = 0))
print(grades.std(axis = 0)) 

#perform operations ON the rows (y-axis is axis 1)
print("\nstats for rows:")
print(grades.sum(axis = 1)) #This gives a 1 by 4 array
print(grades.min(axis = 1))
print(grades.max(axis = 1))
print(grades.mean(axis = 1))
print(grades.std(axis = 1))

print("\nSlicing and Dicing")
print(grades)
#Recall: In bracket notation, we do row first, column 2nd.
print(grades[0,1]) #grade at row 0 col 1
print(grades[1]) #grades in row 1
print(grades[0:2]) #grades in first two rows (excludes row 2)
print(grades[[1,3]]) #how to get nonconsecutive rows:
#here you need 2 brackets because #you are passing #in the list of rows (so [1,3]) #that you want to print
print(grades[:,0]) #gives all rows but just col 0 in each
print(grades[:,1:3]) #gives all rows but just cols 1-2 in each
print(grades[:,[0,2]]) #gives all rows ut just cols 0 and 2 in each

print(grades[:, [-1, -2]])
print(grades[:, [1, -1]])

print(grades.flatten())

transpose = grades.T
print(transpose)

import pandas as pd

df = pd.read_csv('finalgrades.csv')

print("Printing List of the Columns")
print(df.columns)
print("\nPrinting First Few Rows")
print(df.head())
print("\nPrint How Many Rows and Cols")
print(df.shape)

df.index = df["ID"]

print("\nPracticing Getting Data from a DF")
x = df.iloc[4,9] #x is the element in the 5th row, column 10
#because we start counting at 0.
print(x)
labs = df.iloc[:,1:13] #labs contains ALL rows and columns 1:13,
#which corresponds to the lab grades in #the csv file.
print(labs)


labs = df.loc[:,'Lab2':'Lab12'] #We start at Lab2 column and go up to
#AND including the Lab12 column.
print(labs)
hwks = df.loc[:,'HW1':'HW13'] #We start at HW1 column and go up to
#AND including the HW13 column.
print(hwks)

print("\nWho did Best on the Exams")
print("Exam 1")
gradesExam1 = df.sort_values(by='Exam1', ascending = False)
gradesExam1 = gradesExam1.loc[:, "Exam1"]
print(gradesExam1.head()) #Shows the first few values

print("Exam 2")
gradesExam2 = df.sort_values(by='Exam2', ascending = False)
gradesExam2 = gradesExam2.loc[:, "Exam2"]
print(gradesExam2.head()) #Shows the first few values

print("Exam 3")
gradesExam3 = df.sort_values(by='Exam3', ascending = False)
gradesExam3 = gradesExam3.loc[:, "Exam3"]
print(gradesExam3.head()) #Shows the first few values

print("Final Exam")
gradesExamF = df.sort_values(by='FinalExam', ascending = False)
gradesExamF = gradesExamF.loc[:, "FinalExam"]
print(gradesExamF.head()) #Shows the first few values

import matplotlib.pyplot as plt
xBins = np.arange(0,105,5)
#create the histogram
exHistogram = gradesExam1.hist(grid = True, bins = xBins)
plt.title("Exam 1 Grades") #Set its title
plt.show() #Show the histogram
print('\n\n', gradesExam1.describe(), sep='')

exHistogram = gradesExam2.hist(grid = True, bins = xBins)
plt.title("Exam 2 Grades") #Set its title
plt.show() #Show the histogram
print('\n\n', gradesExam2.describe(), sep='')

exHistogram = gradesExam3.hist(grid = True, bins = xBins)
plt.title("Exam 3 Grades") #Set its title
plt.show() #Show the histogram
print('\n\n', gradesExam3.describe(), sep='')

exHistogram = gradesExamF.hist(grid = True, bins = xBins)
plt.title("Exam F Grades") #Set its title
plt.show() #Show the histogram
print('\n\n', gradesExamF.describe(), sep='')

file = open('gradeInfo.txt', 'w+')
file.write('Exam 1 Grades\n' + str(gradesExam1.describe()) + '\n\n')
file.write('Exam 2 Grades\n' + str(gradesExam2.describe()) + '\n\n')
file.write('Exam 3 Grades\n' + str(gradesExam3.describe()) + '\n\n')
file.write('Exam F Grades\n' + str(gradesExamF.describe()) + '\n\n')
file.close()

exams = df.loc[:,'Exam1':'Exam3'] #Zoom in on just the exam cols
df["ExamAvg"] = exams.mean(axis=1) #take the mean of the 3 exams
#for each student. Since we are
#doing an average for each student, #we are focusing in on the y axis,
#so axis 1.
print(df) #You’ll see a new column at the end.

labs = df.loc[:,'Lab2':'Lab12']
df["LabAvg"] =labs.mean(axis=1)*10
print(df)

pre_class = df.loc[:,'Pre-Class1':'Pre-Class22']
df["PreClassAvg"] =pre_class.mean(axis=1)*20
print(df)

pre_class = df.loc[:,'HW1':'HW13']
df["HWAvg"]= (pre_class.sum(axis=1)/100) * 100
print(df)

df["FinalGrade"] = df.loc[:,"LabAvg"] * 0.08 + df.loc[:,"PreClassAvg"] * 0.02 + df.loc[:,"HWAvg"] * 0.15 + df.loc[:,"ExamAvg"] * 0.45 + df.loc[:, "FinalProject"] * 0.15 + df.loc[:, "FinalExam"] * 0.15
print(df)
