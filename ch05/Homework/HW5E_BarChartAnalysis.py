import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statistics as stats

    
''' Attributes for both student-mat-posted.csv (Math course) datasets:
0 school - student's school (binary: "GP" - Gabriel Pereira or "MS" - Mousinho da Silveira)
1 sex - student's sex (binary: "F" - female or "M" - male)
2 age - student's age (numeric: from 15 to 22)
3 Medu - mother's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
4 Fedu - father's education (numeric: 0 - none,  1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)
5 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
6 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
7 activities - extra-curricular activities (binary: yes or no)
8 nursery - attended nursery school (binary: yes or no)
9 higher - wants to take higher education (binary: yes or no)
10 romantic - with a romantic relationship (binary: yes or no)
11 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
12 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
13 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
14 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
15 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
16 health - current health status (numeric: from 1 - very bad to 5 - very good)
17 absences - number of school absences (numeric: from 0 to 93)
18 G1 - first period grade (numeric: on their scale, it's from 0 to 20.  I have converted it to 0 to 100.)
19 G2 - second period grade (numeric: on their scale, it's from 0 to 20.  I have converted it to 0 to 100.)
20 G3 - final grade (numeric: on their scale, it's from 0 to 20.  I have converted it to 0 to 100.)'''


school = [
('GP','F',18,4,4,2,2,'no','yes','yes','no',4,3,4,1,1,3,6,25,30,30),
('GP','F',17,1,1,1,2,'no','no','yes','no',5,3,3,1,1,3,4,25,25,30),
('GP','F',15,1,1,1,2,'no','yes','yes','no',4,3,2,2,3,3,10,35,40,50),
('GP','F',15,4,2,1,3,'yes','yes','yes','yes',3,2,2,1,1,5,2,75,70,75),
('GP','F',16,3,3,1,2,'no','yes','yes','no',4,3,2,1,2,5,4,30,50,50),
('GP','M',16,4,3,1,2,'yes','yes','yes','no',5,4,2,1,2,5,10,75,75,75),
('GP','M',16,2,2,1,2,'no','yes','yes','no',4,4,4,1,1,3,0,60,60,55),
('GP','F',17,4,4,2,2,'no','yes','yes','no',4,1,4,1,1,1,6,30,25,30),
('GP','M',15,3,2,1,2,'no','yes','yes','no',4,2,2,1,1,1,0,80,90,95),
('GP','M',15,3,4,1,2,'yes','yes','yes','no',5,5,1,1,1,5,0,70,75,75),
('GP','F',15,4,4,1,2,'no','yes','yes','no',3,3,3,1,2,2,0,50,40,45),
('GP','F',15,2,1,3,3,'yes','yes','yes','no',5,2,2,1,1,4,4,50,60,60),
('GP','M',15,4,4,1,1,'yes','yes','yes','no',4,3,3,1,3,5,2,70,70,70),
('GP','M',15,4,3,2,2,'no','yes','yes','no',5,4,3,1,2,3,2,50,50,55),
('GP','M',15,2,2,1,3,'no','yes','yes','yes',4,5,2,1,1,3,0,70,80,80),
('GP','F',16,4,4,1,1,'no','yes','yes','no',4,4,4,1,2,2,4,70,70,70),
('GP','F',16,4,4,1,3,'yes','yes','yes','no',3,2,3,1,2,2,6,65,70,70),
('GP','F',16,3,3,3,2,'yes','yes','yes','no',5,3,2,1,1,4,4,40,50,50),
('GP','M',17,3,2,1,1,'yes','yes','yes','no',5,5,5,2,4,5,16,30,25,25),
('GP','M',16,4,3,1,1,'yes','yes','yes','no',3,1,3,1,3,5,4,40,50,50),
('GP','M',15,4,3,1,2,'no','yes','yes','no',4,4,1,1,1,1,0,65,70,75),
('GP','M',15,4,4,1,1,'no','yes','yes','no',5,4,2,1,1,5,0,60,75,75),
('GP','M',16,4,2,1,2,'yes','yes','yes','no',4,5,1,1,3,5,2,75,75,80),
('GP','M',16,2,2,2,2,'yes','yes','yes','no',5,4,4,2,4,5,0,65,65,60),
('GP','F',15,2,4,1,3,'yes','yes','yes','no',4,3,2,1,1,5,2,50,45,40),
('GP','F',16,2,2,1,1,'no','no','yes','no',1,2,2,1,3,5,14,30,45,40),
('GP','M',15,2,2,1,1,'no','yes','yes','no',4,2,2,1,2,5,2,60,60,55),
('GP','M',15,4,2,1,1,'no','yes','yes','no',2,2,4,2,4,1,4,75,80,75),
('GP','M',16,3,4,1,2,'yes','yes','yes','no',5,3,3,1,1,5,4,55,55,55),
('GP','M',16,4,4,1,2,'yes','yes','yes','yes',4,4,5,5,5,5,16,50,60,55),
('GP','M',15,4,4,1,2,'no','no','yes','no',5,4,2,3,4,5,0,45,55,60),
('GP','M',15,4,4,2,2,'yes','yes','yes','no',4,3,1,1,1,5,0,85,80,85),
('GP','M',15,4,3,1,2,'yes','yes','yes','yes',4,5,2,1,1,5,0,85,80,80),
('GP','M',15,3,3,1,2,'yes','no','yes','no',5,3,2,1,1,2,0,40,50,60),
('GP','M',16,3,2,1,1,'no','no','yes','no',5,4,3,1,1,5,0,60,70,75),
('GP','F',15,2,3,2,1,'yes','yes','yes','no',3,5,1,1,1,5,0,40,35,30),
('GP','M',15,4,3,1,3,'yes','yes','yes','no',5,4,3,1,1,4,2,75,80,90),
('GP','M',16,4,4,2,3,'yes','yes','yes','yes',2,4,3,1,1,5,7,75,80,75),
('GP','F',15,3,4,1,3,'yes','yes','yes','no',4,3,2,1,1,5,2,60,60,55),
('GP','F',15,2,2,1,1,'yes','yes','yes','no',4,3,1,1,1,2,8,70,65,65),
('GP','F',16,2,2,2,2,'yes','no','yes','yes',3,3,3,1,2,3,25,35,50,55),
('GP','M',15,4,4,1,1,'no','no','yes','yes',5,4,3,2,4,5,8,60,60,60),
('GP','M',15,4,4,1,2,'yes','yes','yes','no',4,3,3,1,1,5,2,95,90,90),
('GP','M',15,2,2,1,1,'no','yes','yes','no',5,4,1,1,1,1,0,40,40,55),
('GP','F',16,2,2,2,2,'yes','yes','yes','no',4,3,3,2,2,5,14,50,50,45),
('GP','F',15,4,3,1,2,'yes','yes','yes','yes',5,2,2,1,1,5,8,40,40,30),
('GP','F',16,3,3,1,2,'no','yes','yes','no',2,3,5,1,4,3,12,55,60,55),
('GP','M',16,4,3,1,4,'yes','yes','yes','no',4,2,2,1,1,2,4,95,95,100),
('GP','M',15,4,2,1,2,'no','yes','yes','no',4,3,3,2,2,5,2,75,75,70),
('GP','F',15,4,4,1,2,'yes','no','yes','no',4,4,4,1,1,3,2,35,35,35),
('GP','F',16,2,2,3,2,'no','yes','yes','no',4,3,3,2,3,4,2,60,65,65),
('GP','F',15,4,2,1,2,'no','yes','yes','no',4,3,3,1,1,5,2,55,65,65),
('GP','M',15,4,2,2,1,'no','yes','yes','no',5,5,5,3,4,5,6,55,55,50),
('GP','F',15,4,4,1,1,'no','yes','yes','no',3,3,4,2,3,5,0,40,50,55),
('GP','F',15,3,3,1,1,'no','yes','yes','no',5,3,4,4,4,1,6,50,65,65),
('GP','F',16,2,1,1,2,'yes','yes','yes','yes',5,3,4,1,1,2,8,40,45,50),
('GP','F',15,4,3,1,2,'yes','yes','yes','no',4,3,2,1,1,1,0,70,75,75),
('GP','M',15,4,4,1,2,'yes','yes','yes','no',3,2,2,1,1,5,4,70,75,75),
('GP','M',15,1,2,1,2,'yes','yes','yes','no',4,3,2,1,1,5,2,45,50,45),
('GP','F',16,4,2,1,2,'no','yes','yes','no',4,2,3,1,1,5,2,75,80,80),
('GP','F',16,4,4,1,2,'yes','yes','yes','no',2,4,4,2,3,4,6,50,55,55),
('GP','F',16,1,1,4,1,'yes','no','yes','yes',5,5,5,5,5,5,6,50,40,55),
('GP','F',16,1,2,1,2,'yes','yes','yes','no',4,4,3,1,1,1,4,40,50,45),
('GP','F',16,4,3,1,3,'yes','yes','yes','no',3,4,4,2,4,4,2,50,45,45),
('GP','F',15,4,3,1,2,'yes','yes','yes','yes',4,4,4,2,4,2,0,50,50,50),
('GP','F',16,4,3,3,2,'yes','yes','yes','no',5,4,3,1,2,1,2,80,75,75),
('GP','M',15,4,4,1,4,'yes','no','yes','yes',1,3,3,5,5,3,4,65,65,60),
('GP','F',16,3,1,1,4,'no','yes','yes','no',4,3,3,1,2,5,4,35,35,30),
('GP','F',15,2,2,2,2,'no','yes','yes','no',4,1,3,1,3,4,2,40,45,40),
('GP','F',15,3,1,2,4,'no','no','yes','no',4,4,2,2,3,3,12,80,80,80),
('GP','M',16,3,1,2,4,'no','yes','yes','no',4,3,2,1,1,5,0,65,75,75),
('GP','M',15,4,2,1,4,'no','yes','yes','no',3,3,3,1,1,3,0,50,50,50),
('GP','F',15,1,1,1,2,'no','no','yes','yes',3,3,4,2,4,5,2,40,30,25),
('GP','M',16,3,1,1,1,'yes','yes','yes','no',5,3,2,2,2,5,2,60,60,70),
('GP','F',16,3,3,1,2,'yes','yes','yes','no',4,3,3,2,4,5,54,55,60,55),
('GP','M',15,4,3,1,2,'yes','yes','yes','no',4,3,3,2,3,5,6,45,45,50),
('GP','M',15,4,0,2,4,'yes','yes','yes','no',3,4,3,1,1,1,8,55,55,50),
('GP','F',16,2,2,1,4,'no','yes','yes','yes',5,2,3,1,3,3,0,55,55,55),
('GP','M',17,2,1,2,1,'yes','yes','no','no',4,5,1,1,1,3,2,40,40,50),
('GP','F',16,3,4,1,2,'no','yes','yes','no',2,4,3,1,2,3,12,25,25,25),
('GP','M',15,2,3,1,1,'yes','no','yes','yes',3,2,2,1,3,3,2,50,60,60),
('GP','M',15,2,3,1,3,'no','no','yes','no',5,3,2,1,2,5,4,55,50,55),
('GP','F',15,3,2,1,2,'no','yes','yes','no',4,4,4,1,1,5,10,35,30,30),
('GP','M',15,2,2,2,2,'yes','yes','yes','no',5,3,3,1,3,4,4,75,75,75),
('GP','F',15,1,1,1,2,'yes','no','yes','no',4,3,2,2,3,4,2,45,50,50),
('GP','F',15,4,4,2,2,'no','yes','yes','yes',4,4,4,2,3,5,6,35,45,40),
('GP','F',16,2,2,1,2,'no','yes','yes','no',4,3,4,1,2,2,4,40,35,30),
('GP','F',15,4,2,1,3,'yes','yes','yes','no',5,3,3,1,3,1,4,65,70,70),
('GP','M',16,2,2,2,2,'yes','no','yes','no',4,4,2,1,1,3,12,55,50,50),
('GP','M',16,4,4,1,2,'no','yes','yes','no',4,1,3,3,5,5,18,40,30,35),
('GP','F',16,3,3,1,3,'no','yes','yes','yes',4,3,3,1,3,4,0,35,35,40),
('GP','F',15,4,3,1,1,'yes','yes','yes','no',4,5,5,1,3,1,4,80,85,90),
('GP','F',16,3,1,1,2,'no','yes','yes','no',3,3,3,2,3,2,4,35,30,30),
('GP','F',16,4,2,2,2,'yes','yes','yes','no',5,3,3,1,1,1,0,55,50,50),
('GP','M',15,2,2,1,4,'yes','yes','yes','no',4,3,4,1,1,4,6,55,65,70),
('GP','F',15,1,1,2,4,'yes','yes','yes','no',3,1,2,1,1,1,2,35,50,50),
('GP','M',16,4,3,2,1,'yes','no','yes','no',3,3,3,1,1,4,2,55,75,75),
('GP','F',16,2,1,1,2,'no','yes','yes','yes',4,3,5,1,1,5,2,40,45,50),
('GP','F',16,4,4,1,1,'yes','no','yes','no',5,3,4,1,2,1,6,55,70,70),
('GP','F',16,4,3,1,3,'no','yes','yes','no',5,3,5,1,1,3,0,35,45,40),
('GP','M',16,4,4,1,1,'yes','yes','yes','no',4,5,5,5,5,4,14,35,35,25),
('GP','M',16,4,4,1,3,'yes','yes','yes','yes',4,4,3,1,1,4,0,80,85,85),
('GP','M',15,4,4,1,1,'yes','no','yes','no',5,3,3,1,1,5,4,50,65,70),
('GP','F',15,3,2,2,2,'no','yes','yes','no',4,3,5,1,1,2,26,35,30,30),
('GP','M',15,3,4,1,2,'yes','yes','yes','no',5,4,4,1,1,1,0,80,90,90),
('GP','F',15,3,3,1,4,'no','yes','yes','no',4,3,3,1,1,4,10,50,55,55),
('GP','F',15,2,2,1,4,'no','yes','yes','no',5,1,2,1,1,3,8,35,40,40),
('GP','M',16,3,3,1,3,'yes','yes','yes','no',5,3,3,1,1,5,2,80,90,90),
('GP','M',15,4,4,4,4,'yes','yes','yes','yes',1,3,5,3,5,1,6,50,65,65),
('GP','F',16,4,4,1,3,'yes','yes','yes','yes',5,4,5,1,1,4,4,70,75,80),
('GP','M',15,4,4,1,1,'yes','yes','yes','no',5,5,3,1,1,4,6,90,95,95),
('GP','F',16,3,3,1,3,'yes','yes','yes','no',4,1,2,1,1,2,0,35,50,50),
('GP','F',16,2,2,1,2,'yes','yes','yes','no',3,1,2,1,1,5,6,50,65,65),
('GP','M',15,4,2,1,1,'no','yes','yes','no',3,5,2,1,1,3,10,90,95,95),
('GP','M',15,2,1,1,2,'yes','yes','yes','yes',5,4,2,1,1,5,8,45,45,45),
('GP','M',16,4,4,1,2,'yes','yes','yes','no',5,4,4,1,2,5,2,75,75,80),
('GP','M',15,4,4,2,2,'yes','yes','yes','no',4,4,3,1,1,2,2,55,65,70),
('GP','M',16,3,3,2,1,'yes','yes','yes','no',5,4,2,1,1,5,0,65,70,65),
('GP','M',17,1,3,3,2,'yes','yes','yes','no',5,2,4,1,4,5,20,45,35,40),
('GP','M',15,3,4,1,1,'no','yes','yes','no',3,4,3,1,2,4,6,70,65,65),
('GP','F',15,1,2,1,2,'no','no','yes','no',3,2,3,1,2,1,2,80,75,75),
('GP','M',15,2,2,1,4,'yes','yes','yes','no',5,5,4,1,2,5,6,80,70,75),
('GP','F',16,2,4,2,2,'yes','yes','yes','yes',4,2,2,1,2,5,2,65,65,65),
('GP','M',16,4,4,1,1,'yes','yes','yes','no',3,4,4,1,4,5,18,70,55,65),
('GP','F',16,2,2,1,2,'no','yes','yes','yes',5,4,4,1,1,5,0,40,35,40),
('GP','M',15,3,4,1,1,'no','yes','yes','no',5,5,5,3,2,5,0,65,65,60),
('GP','F',15,3,4,1,2,'yes','yes','yes','yes',5,3,2,1,1,1,0,35,50,55),
('GP','F',19,0,1,1,2,'no','no','no','no',3,4,2,1,1,5,2,35,40,45),
('GP','M',18,2,2,1,1,'yes','yes','yes','no',3,3,3,1,2,4,0,35,20,0),
('GP','M',16,4,4,1,1,'yes','yes','yes','no',3,5,5,2,5,4,8,90,90,90),
('GP','F',15,3,4,2,3,'no','yes','yes','yes',4,2,2,2,2,5,0,60,0,0),
('GP','F',15,1,1,3,1,'yes','no','yes','yes',4,3,3,1,2,4,0,40,0,0),
('GP','F',17,2,2,1,1,'no','yes','yes','yes',3,4,4,1,3,5,12,50,65,60),
('GP','F',16,3,4,1,1,'no','yes','yes','no',3,2,1,1,4,5,16,60,55,55),
('GP','M',15,3,4,4,2,'no','yes','yes','yes',5,3,3,1,1,5,0,45,0,0),
('GP','F',15,4,4,1,3,'yes','yes','yes','yes',4,3,3,1,1,5,0,55,0,0),
('GP','M',17,3,4,3,2,'no','yes','yes','no',5,4,5,2,4,5,0,50,0,0),
('GP','F',16,3,3,2,1,'yes','no','yes','yes',4,3,2,1,1,5,0,20,0,0),
('GP','M',16,1,1,1,2,'no','yes','yes','yes',4,4,4,1,3,5,0,70,60,60),
('GP','F',15,4,4,2,1,'yes','yes','yes','no',4,3,2,1,1,5,0,80,80,75),
('GP','M',15,4,3,2,4,'no','yes','yes','no',2,2,2,1,1,3,0,35,45,0),
('GP','M',16,2,2,2,1,'yes','yes','yes','no',2,3,3,2,2,2,8,45,45,45),
('GP','F',15,4,4,1,3,'yes','yes','yes','no',4,2,2,1,1,5,2,45,55,55),
('GP','F',16,1,1,1,1,'no','yes','yes','no',3,4,4,3,3,1,2,70,70,65),
('GP','M',17,2,1,1,1,'no','yes','yes','no',5,4,5,1,2,5,0,25,0,0),
('GP','F',15,1,1,1,2,'no','yes','yes','no',4,4,2,1,2,5,0,40,55,55),
('GP','F',15,3,2,1,2,'no','yes','yes','no',3,3,2,1,1,3,0,30,35,0),
('GP','F',15,1,2,1,2,'no','no','yes','no',4,3,2,1,1,5,2,50,55,55),
('GP','M',16,4,4,1,1,'no','yes','no','yes',3,3,2,2,1,5,0,35,30,0),
('GP','M',15,2,1,4,1,'no','yes','yes','no',4,5,5,2,5,5,0,40,45,50),
('GP','M',18,1,1,1,1,'no','yes','no','yes',2,3,5,2,5,4,0,30,25,0),
('GP','M',16,2,1,1,1,'yes','yes','yes','yes',4,4,4,3,5,5,6,60,65,70),
('GP','F',15,3,3,2,3,'yes','yes','yes','yes',4,2,1,2,3,3,8,50,50,50),
('GP','M',19,3,2,1,1,'no','yes','no','yes',4,5,4,1,1,4,0,25,0,0),
('GP','F',17,4,4,1,1,'no','yes','yes','yes',4,2,1,1,1,4,0,55,55,60),
('GP','M',15,2,3,1,2,'yes','yes','yes','no',4,4,4,1,1,1,2,55,40,40),
('GP','M',17,1,2,1,1,'no','yes','yes','no',2,2,2,3,3,5,8,80,60,65),
('GP','F',18,1,1,3,1,'yes','no','yes','no',5,2,5,1,5,4,6,45,40,50),
('GP','M',16,2,2,3,1,'no','no','yes','no',4,2,2,1,2,3,2,85,75,75),
('GP','M',16,3,3,1,2,'no','yes','yes','yes',4,5,5,4,4,5,4,50,60,60),
('GP','M',17,2,1,2,1,'yes','yes','no','yes',3,3,2,2,2,5,0,35,30,0),
('GP','M',15,3,2,2,2,'no','yes','yes','yes',4,4,4,1,4,3,6,25,45,35),
('GP','M',16,1,2,2,1,'yes','yes','yes','no',4,4,4,2,4,5,0,35,0,0),
('GP','M',17,1,3,1,1,'no','yes','no','no',5,3,3,1,4,2,2,50,50,50),
('GP','M',17,1,1,4,2,'yes','yes','no','yes',5,3,5,1,5,5,0,25,40,35),
('GP','M',16,3,2,2,1,'yes','no','no','no',4,5,2,1,1,2,16,60,55,60),
('GP','M',16,2,2,1,2,'no','yes','no','no',4,3,5,2,4,4,4,50,50,50),
('GP','F',16,4,2,1,2,'no','yes','yes','yes',4,2,3,1,1,3,0,70,75,80),
('GP','F',16,2,2,1,2,'no','no','yes','no',5,1,5,1,1,4,0,30,35,0),
('GP','F',16,4,4,1,2,'no','yes','yes','yes',4,4,2,1,1,3,0,70,70,70),
('GP','M',16,3,4,3,1,'yes','no','yes','no',3,4,5,2,4,2,0,30,25,0),
('GP','M',16,1,0,2,2,'yes','yes','yes','yes',4,3,2,1,1,3,2,65,75,80),
('GP','M',17,4,4,1,2,'yes','yes','yes','no',4,4,4,1,3,5,0,65,55,50),
('GP','F',16,1,3,1,2,'yes','no','yes','yes',4,3,5,1,1,3,0,40,35,0),
('GP','F',16,3,3,2,2,'yes','yes','yes','no',4,4,5,1,1,4,4,50,55,45),
('GP','M',17,4,3,2,2,'yes','yes','yes','no',4,4,4,4,4,4,4,50,45,45),
('GP','F',16,2,2,2,2,'yes','no','yes','no',3,4,4,1,4,5,2,65,65,55),
('GP','M',17,3,3,1,2,'yes','no','yes','no',4,3,4,1,4,4,4,30,25,30),
('GP','M',16,4,2,1,1,'yes','yes','yes','yes',4,3,3,3,4,3,10,50,40,45),
('GP','M',17,4,3,1,2,'yes','yes','yes','yes',5,2,3,1,1,2,4,50,50,55),
('GP','M',16,4,3,1,2,'yes','yes','yes','no',3,4,3,2,3,3,10,45,40,40),
('GP','M',16,3,3,1,2,'yes','yes','yes','yes',4,2,3,1,2,3,2,60,65,60),
('GP','F',17,2,4,1,2,'yes','yes','yes','no',5,4,2,2,3,5,0,80,85,85),
('GP','F',17,3,3,1,2,'yes','yes','yes','yes',5,3,3,2,3,1,56,45,45,40),
('GP','F',16,3,2,1,2,'no','yes','yes','no',1,2,2,1,2,1,14,60,65,60),
('GP','M',17,3,3,1,2,'yes','yes','yes','yes',4,3,4,2,3,4,12,60,60,55),
('GP','M',16,1,2,1,1,'yes','yes','yes','yes',3,3,3,1,2,3,2,55,60,55),
('GP','M',16,2,1,1,2,'yes','yes','yes','yes',4,2,3,1,2,5,0,75,75,75),
('GP','F',17,3,3,1,2,'no','no','yes','yes',3,3,3,1,3,3,6,40,35,45),
('GP','M',17,1,2,1,2,'no','yes','yes','no',3,1,3,1,5,3,4,40,45,50),
('GP','F',16,2,3,1,2,'no','yes','yes','no',4,3,3,1,1,2,10,55,60,65),
('GP','F',17,1,1,1,2,'yes','yes','yes','no',5,3,3,1,1,3,0,40,40,45),
('GP','M',17,1,2,2,2,'yes','no','yes','no',4,4,4,4,5,5,12,35,40,40),
('GP','M',16,3,3,1,1,'yes','yes','yes','no',4,3,2,3,4,5,8,40,45,50),
('GP','M',16,2,3,2,1,'no','yes','yes','no',5,3,3,1,1,3,0,65,70,70),
('GP','F',17,2,4,1,2,'yes','yes','yes','yes',4,3,2,1,1,5,0,70,75,75),
('GP','M',17,4,4,1,1,'no','yes','yes','no',5,2,3,1,2,5,4,85,75,80),
('GP','M',16,3,3,3,1,'yes','yes','yes','no',3,3,4,3,5,3,8,45,45,50),
('GP','F',17,4,4,2,1,'no','yes','yes','no',4,2,4,2,3,2,24,90,90,90),
('GP','F',16,4,4,1,2,'no','yes','yes','no',4,5,2,1,2,3,0,45,45,50),
('GP','F',16,4,3,1,2,'yes','yes','yes','no',4,3,5,1,5,2,2,80,80,80),
('GP','F',16,2,3,1,2,'yes','yes','yes','no',4,4,3,1,3,4,6,40,50,50),
('GP','F',17,1,1,1,2,'no','no','yes','no',4,4,4,1,3,1,4,45,45,50),
('GP','F',17,2,2,1,1,'no','yes','yes','no',5,3,2,1,2,3,18,35,30,30),
('GP','F',16,2,2,2,4,'yes','no','yes','no',5,3,5,1,1,5,6,50,50,55),
('GP','F',17,3,4,1,3,'no','yes','yes','yes',4,4,3,3,4,5,28,50,45,45),
('GP','F',16,3,1,1,2,'no','yes','yes','no',2,3,3,2,2,4,5,35,35,35),
('GP','F',16,4,3,1,2,'yes','yes','yes','yes',1,3,2,1,1,1,10,55,60,65),
('GP','F',16,1,1,2,1,'no','yes','yes','no',4,3,2,1,4,5,6,45,45,50),
('GP','F',17,4,3,2,3,'yes','yes','yes','yes',4,4,2,1,1,4,6,35,35,35),
('GP','F',19,3,3,1,4,'yes','yes','yes','no',4,3,3,1,2,3,10,40,40,40),
('GP','M',17,4,4,1,2,'no','yes','yes','yes',5,3,5,4,5,3,13,60,60,65),
('GP','F',16,2,2,1,2,'no','yes','yes','no',3,3,4,1,1,4,0,60,65,70),
('GP','M',18,2,2,1,2,'yes','yes','yes','no',4,4,4,2,4,5,15,30,35,40),
('GP','F',17,4,4,1,1,'no','yes','yes','no',5,2,1,1,2,3,12,40,50,50),
('GP','F',17,3,2,2,2,'no','yes','yes','no',4,4,4,1,3,1,2,70,75,75),
('GP','F',17,4,3,1,2,'no','yes','yes','yes',3,4,5,2,4,1,22,30,30,20),
('GP','M',18,3,3,1,2,'no','yes','yes','no',3,2,4,2,4,4,13,30,30,40),
('GP','F',17,2,3,2,1,'no','yes','yes','no',3,3,3,1,4,3,3,35,35,40),
('GP','F',17,2,2,1,3,'yes','yes','yes','no',4,3,3,1,1,4,4,45,50,50),
('GP','F',17,2,1,2,2,'yes','yes','yes','no',4,2,5,1,2,5,2,30,30,30),
('GP','F',17,1,1,1,3,'yes','yes','yes','yes',4,3,4,1,1,5,0,30,25,0),
('GP','F',16,2,3,1,2,'no','yes','yes','no',2,3,1,1,1,3,2,80,80,85),
('GP','M',18,2,2,2,2,'no','yes','yes','no',3,3,3,5,5,4,0,60,65,65),
('GP','F',16,4,4,1,3,'yes','no','yes','no',5,3,2,1,1,5,0,65,65,70),
('GP','F',18,3,1,1,2,'yes','yes','yes','yes',5,3,3,1,1,4,16,45,40,35),
('GP','F',17,3,2,1,2,'yes','no','yes','no',5,3,4,1,3,3,10,80,75,75),
('GP','M',17,2,3,1,2,'no','no','yes','no',5,3,3,1,3,3,2,60,55,60),
('GP','M',18,2,1,4,2,'yes','yes','yes','yes',4,3,2,4,5,3,14,50,40,45),
('GP','F',17,2,1,2,3,'yes','yes','yes','yes',3,2,3,1,2,3,10,60,50,60),
('GP','F',17,4,3,1,2,'yes','yes','yes','yes',3,2,3,1,2,3,14,65,65,70),
('GP','M',17,2,2,2,2,'yes','yes','yes','no',4,5,2,1,1,1,4,55,55,55),
('GP','M',17,4,4,1,2,'yes','yes','yes','yes',4,5,5,1,3,2,14,55,45,45),
('GP','M',16,4,4,1,2,'yes','yes','yes','no',4,2,4,2,4,1,2,70,65,65),
('GP','M',16,1,1,2,2,'no','yes','yes','no',3,4,2,1,1,5,18,45,35,30),
('GP','M',16,3,2,2,3,'yes','yes','yes','yes',5,3,3,1,3,2,10,55,45,50),
('GP','M',17,2,2,1,2,'yes','no','yes','yes',4,4,2,5,5,4,4,70,65,65),
('GP','F',16,2,1,1,1,'no','yes','yes','yes',4,5,2,1,1,5,20,65,60,60),
('GP','F',17,2,1,3,2,'yes','yes','yes','no',2,1,1,1,1,3,2,65,55,55),
('GP','M',18,2,2,1,2,'no','yes','no','no',5,5,4,3,5,2,0,35,35,0),
('GP','M',17,4,3,2,2,'yes','yes','yes','yes',2,5,5,1,4,5,14,60,60,60),
('GP','M',17,4,4,2,2,'no','yes','yes','no',3,3,3,2,3,4,2,50,55,60),
('GP','M',16,4,3,1,1,'yes','no','yes','no',5,4,5,1,1,3,0,30,0,0),
('GP','M',16,4,4,1,1,'yes','yes','yes','no',5,3,2,1,2,5,0,65,60,60),
('GP','F',18,2,1,2,3,'no','no','yes','yes',4,4,4,1,1,3,0,35,0,0),
('GP','M',16,2,1,3,1,'no','yes','yes','no',4,3,3,1,1,4,6,90,90,90),
('GP','M',17,2,3,2,1,'no','yes','yes','no',5,2,2,1,1,2,4,60,60,65),
('GP','M',22,3,1,1,1,'no','no','no','yes',5,4,5,5,5,1,16,30,40,40),
('GP','M',18,3,3,1,2,'no','yes','yes','yes',4,3,3,1,3,5,8,15,25,25),
('GP','M',16,0,2,1,1,'no','no','yes','no',4,3,2,2,4,5,0,65,75,75),
('GP','M',18,3,2,2,1,'no','yes','no','no',4,4,5,2,4,5,0,30,40,40),
('GP','M',16,3,3,3,2,'no','no','yes','no',5,3,3,1,3,2,6,35,50,50),
('GP','M',18,2,1,1,1,'no','no','no','no',3,2,5,2,5,5,4,30,45,40),
('GP','M',16,2,1,2,1,'yes','no','yes','no',3,3,2,1,3,3,0,40,45,40),
('GP','M',17,2,1,1,1,'no','no','yes','no',4,4,2,2,4,5,0,40,60,60),
('GP','M',17,1,1,2,1,'yes','yes','yes','no',4,4,4,1,2,5,2,35,45,40),
('GP','F',17,4,2,1,4,'yes','yes','yes','no',4,2,3,1,1,4,6,70,60,65),
('GP','M',19,4,3,1,2,'no','yes','yes','no',4,3,1,1,1,1,12,55,55,55),
('GP','M',18,2,1,1,2,'yes','yes','yes','no',5,2,4,1,2,4,8,75,70,70),
('GP','F',17,2,2,1,4,'yes','yes','yes','yes',3,4,1,1,1,2,0,50,45,0),
('GP','F',18,4,3,1,2,'no','yes','yes','yes',3,1,2,1,3,2,21,85,90,90),
('GP','M',18,4,3,1,2,'no','no','yes','no',4,3,2,1,1,3,2,40,40,40),
('GP','M',18,3,2,1,3,'yes','no','yes','no',5,3,2,1,1,3,1,65,60,60),
('GP','F',17,3,3,1,3,'yes','no','yes','no',3,2,3,1,1,4,4,50,45,45),
('GP','F',18,2,2,1,3,'yes','yes','yes','yes',4,3,3,1,1,3,0,45,50,0),
('GP','M',18,3,4,2,2,'yes','yes','yes','no',4,2,5,3,4,1,13,85,85,85),
('GP','M',17,3,1,1,2,'yes','yes','yes','yes',5,4,4,3,4,5,2,45,45,50),
('GP','F',18,4,4,2,2,'yes','yes','yes','no',4,3,4,2,2,4,8,60,50,55),
('GP','M',18,4,2,1,2,'yes','yes','yes','yes',5,4,5,1,3,5,10,50,45,50),
('GP','F',18,2,1,2,2,'no','yes','no','yes',4,3,5,1,2,3,0,30,0,0),
('GP','F',19,3,3,1,2,'yes','yes','yes','no',4,3,5,3,3,5,15,45,45,45),
('GP','F',18,2,3,1,4,'yes','yes','yes','yes',4,5,5,1,3,2,4,75,70,70),
('GP','F',18,1,1,2,2,'no','no','yes','no',4,4,3,1,1,3,2,55,55,55),
('GP','M',17,1,2,1,2,'yes','no','yes','yes',3,5,2,2,2,1,2,75,70,70),
('GP','F',17,2,4,2,2,'no','yes','yes','yes',4,3,3,1,1,1,2,50,50,50),
('GP','F',17,2,2,2,2,'no','yes','yes','yes',4,4,4,2,3,5,6,60,60,60),
('GP','F',18,3,2,2,2,'no','no','no','yes',4,1,1,1,1,5,75,50,45,45),
('GP','M',18,4,4,2,1,'yes','yes','yes','no',3,2,4,1,4,3,22,45,45,45),
('GP','F',18,4,4,1,2,'yes','yes','yes','yes',2,4,4,1,1,4,15,45,40,40),
('GP','M',18,4,3,2,1,'yes','yes','yes','no',4,2,3,1,2,1,8,50,55,50),
('GP','M',17,4,1,2,1,'yes','yes','yes','yes',4,5,4,2,4,5,30,40,40,40),
('GP','M',17,3,2,1,1,'no','yes','yes','no',4,4,4,3,4,3,19,55,45,50),
('GP','F',18,1,1,2,4,'yes','yes','yes','no',5,2,2,1,1,3,1,60,60,60),
('GP','F',18,1,1,2,2,'yes','yes','yes','no',5,4,4,1,1,4,4,40,45,50),
('GP','F',17,2,2,1,2,'no','no','yes','no',5,4,5,1,2,5,4,50,45,55),
('GP','M',17,1,1,1,2,'no','no','yes','no',4,3,3,1,2,4,2,60,50,55),
('GP','F',18,2,2,1,3,'no','yes','yes','no',4,3,3,1,2,2,5,90,90,95),
('GP','F',17,1,1,1,3,'no','yes','yes','no',4,3,3,1,1,3,6,65,60,60),
('GP','M',18,2,1,1,3,'yes','yes','yes','no',4,2,4,1,3,2,6,75,70,70),
('GP','M',18,4,4,1,2,'yes','yes','yes','no',5,4,3,1,1,2,9,75,65,75),
('GP','M',18,4,2,1,2,'yes','yes','yes','yes',4,3,2,1,4,5,11,60,55,55),
('GP','F',17,4,3,1,3,'no','yes','yes','no',4,2,2,1,2,3,0,75,75,75),
('GP','F',18,2,1,1,2,'no','yes','yes','yes',5,4,3,1,1,5,12,60,60,65),
('GP','F',17,3,1,2,4,'no','yes','yes','no',3,1,2,1,1,3,6,90,90,90),
('GP','M',18,3,2,2,3,'yes','yes','yes','no',5,4,2,1,1,4,8,70,65,70),
('GP','M',17,3,3,1,1,'no','yes','yes','no',4,4,3,1,3,5,4,70,60,55),
('GP','F',19,4,4,2,2,'yes','yes','yes','no',2,3,4,2,3,2,0,50,45,0),
('GP','F',18,4,3,2,2,'no','yes','yes','yes',4,4,5,1,2,2,10,50,40,40),
('GP','F',18,4,3,1,4,'no','yes','yes','no',4,3,3,1,1,3,0,70,65,70),
('GP','M',18,4,4,1,1,'no','yes','yes','yes',1,4,2,2,2,1,5,80,75,80),
('GP','F',18,4,4,1,2,'no','yes','yes','yes',4,2,4,1,1,4,14,60,50,55),
('GP','M',17,4,4,2,1,'no','yes','yes','no',4,1,1,2,2,5,0,55,55,50),
('GP','F',17,4,2,2,3,'no','yes','yes','no',4,3,3,1,1,3,0,75,60,70),
('GP','F',17,3,2,1,4,'yes','no','yes','no',5,2,2,1,2,5,0,85,85,90),
('GP','M',19,3,3,1,2,'yes','yes','yes','yes',4,4,4,1,1,3,20,75,70,65),
('GP','F',18,2,4,1,2,'yes','yes','yes','no',4,4,3,1,1,3,8,70,60,60),
('GP','M',20,3,2,1,1,'yes','yes','yes','no',5,5,3,1,1,5,0,85,90,90),
('GP','M',19,4,4,2,1,'no','yes','yes','yes',4,3,4,1,1,4,38,40,45,40),
('GP','M',19,3,3,1,2,'yes','yes','yes','yes',4,5,3,1,2,5,0,75,60,60),
('GP','F',19,1,1,1,2,'yes','no','yes','no',4,4,3,1,3,3,18,60,50,50),
('GP','F',19,1,2,1,2,'yes','no','yes','yes',4,2,4,2,2,3,0,45,45,0),
('GP','F',19,2,1,3,2,'no','yes','no','yes',3,4,1,1,1,2,20,70,60,65),
('GP','M',19,1,2,1,2,'no','no','yes','no',4,5,2,2,2,4,3,65,55,55),
('GP','F',19,3,2,2,2,'no','no','yes','yes',4,2,2,1,2,1,22,65,50,55),
('GP','F',19,1,1,1,3,'no','no','yes','yes',4,1,2,1,1,3,14,75,65,65),
('GP','F',19,2,3,1,3,'no','yes','yes','yes',4,1,2,1,1,3,40,65,55,55),
('GP','F',18,2,1,2,2,'yes','yes','yes','no',5,3,3,1,2,1,0,40,40,0),
('GP','F',18,4,3,1,3,'yes','yes','yes','yes',4,3,4,1,1,5,9,45,50,45),
('GP','F',17,3,4,1,3,'yes','no','yes','no',4,3,4,2,5,5,0,55,55,50),
('GP','F',18,4,4,1,2,'no','yes','yes','no',4,4,4,3,3,5,2,55,55,55),
('GP','F',17,4,3,1,2,'no','yes','yes','yes',5,2,2,1,2,5,23,65,65,65),
('GP','F',17,2,2,1,2,'no','yes','yes','yes',4,2,2,1,1,3,12,55,45,45),
('GP','F',17,2,2,1,3,'yes','yes','yes','no',3,3,2,2,2,3,3,55,55,55),
('GP','F',17,3,1,1,3,'no','no','yes','no',3,4,3,2,3,5,1,60,70,75),
('GP','F',17,0,2,2,3,'no','yes','yes','no',3,3,3,2,3,2,0,80,75,75),
('GP','M',18,4,4,1,3,'yes','yes','yes','no',4,3,3,2,2,3,3,45,60,55),
('GP','M',17,3,3,1,1,'yes','no','yes','no',4,3,5,3,5,5,3,70,75,80),
('GP','M',17,2,2,4,1,'no','yes','yes','no',4,4,5,5,5,4,8,55,50,50),
('GP','F',17,4,4,1,3,'yes','yes','yes','no',5,4,4,1,3,4,7,50,45,45),
('GP','F',17,4,4,2,3,'no','no','yes','yes',4,3,3,1,2,4,4,70,70,70),
('GP','M',18,2,2,1,4,'yes','yes','yes','no',4,5,5,2,4,5,2,45,40,40),
('GP','F',17,2,4,1,3,'no','yes','yes','yes',4,4,3,1,1,5,7,60,70,70),
('GP','F',18,3,3,1,2,'yes','yes','yes','no',5,3,4,1,1,4,0,35,0,0),
('GP','F',18,2,2,1,2,'yes','no','yes','yes',4,3,3,1,1,2,0,40,40,0),
('GP','F',18,2,2,2,4,'yes','yes','yes','no',4,4,4,1,1,4,0,50,45,0),
('GP','F',17,3,4,1,3,'no','yes','yes','no',4,4,5,1,3,5,16,80,75,75),
('GP','F',19,3,1,1,3,'no','yes','yes','no',5,4,3,1,2,5,12,70,65,65),
('GP','F',17,3,2,1,2,'no','yes','yes','yes',4,3,2,2,3,2,0,35,40,0),
('GP','F',18,3,3,1,4,'no','yes','yes','no',5,3,3,1,1,1,7,80,75,85),
('GP','F',17,3,2,1,2,'no','yes','yes','no',4,3,3,2,3,2,4,45,50,50),
('GP','F',19,2,1,1,3,'yes','yes','yes','yes',4,3,4,1,3,3,4,55,60,55),
('GP','M',18,4,4,1,2,'yes','yes','yes','no',4,3,3,2,2,2,0,50,50,0),
('GP','M',18,3,4,1,2,'yes','yes','yes','yes',4,3,3,1,3,5,11,80,75,75),
('GP','F',17,2,2,1,2,'no','yes','yes','yes',3,3,1,1,2,4,0,45,40,0),
('GP','F',18,2,3,1,3,'no','yes','yes','no',4,3,3,1,2,3,4,55,50,50),
('GP','F',18,3,2,1,3,'no','yes','yes','yes',5,4,3,2,3,1,7,65,65,70),
('GP','M',18,4,3,1,3,'no','yes','yes','yes',5,3,2,1,2,4,9,80,75,80),
('GP','M',18,4,3,1,3,'no','yes','yes','yes',5,4,5,2,3,5,0,50,50,45),
('GP','F',17,4,3,1,3,'yes','yes','yes','yes',4,4,3,1,3,4,0,65,75,75),
('MS','M',18,3,2,2,1,'no','no','yes','no',2,5,5,5,5,5,10,55,65,65),
('MS','M',19,1,1,3,2,'no','yes','yes','no',5,4,4,3,3,2,8,40,35,40),
('MS','M',17,3,3,2,2,'no','yes','yes','no',4,5,4,2,3,3,2,65,65,65),
('MS','M',18,1,3,1,1,'no','yes','no','yes',4,3,3,2,3,3,7,40,35,40),
('MS','M',19,1,1,3,1,'no','yes','yes','no',4,4,4,3,3,5,4,40,40,40),
('MS','M',17,4,3,2,2,'yes','no','yes','yes',4,5,5,1,3,2,4,65,55,55),
('MS','F',18,3,3,1,2,'no','yes','yes','yes',5,3,4,1,1,5,0,50,45,45),
('MS','F',17,4,4,2,2,'yes','yes','yes','no',4,3,3,1,2,5,4,60,65,65),
('MS','F',17,3,2,2,2,'no','yes','yes','yes',1,2,3,1,2,5,2,60,60,55),
('MS','M',18,1,1,2,1,'no','no','yes','yes',3,3,2,1,2,3,4,50,50,50),
('MS','F',18,1,1,2,3,'no','yes','yes','no',5,3,2,1,1,4,0,90,80,80),
('MS','F',18,1,4,3,2,'no','yes','yes','yes',4,3,4,1,4,5,0,65,65,65),
('MS','M',18,1,1,2,2,'yes','no','no','no',4,4,3,2,3,5,2,65,60,60),
('MS','F',18,3,3,2,2,'no','yes','yes','yes',4,3,2,1,3,3,0,55,55,50),
('MS','F',17,4,4,1,2,'yes','yes','yes','yes',2,3,4,1,1,1,0,80,75,75),
('MS','F',17,1,2,2,2,'no','no','yes','no',3,2,2,1,2,3,0,60,55,60),
('MS','M',18,1,3,2,2,'no','yes','yes','no',3,3,4,2,4,3,4,50,50,50),
('MS','M',18,4,4,2,3,'no','yes','yes','yes',4,2,2,2,2,5,0,65,65,65),
('MS','F',17,1,1,3,1,'no','yes','yes','yes',5,2,1,1,2,1,0,35,30,0),
('MS','F',18,2,3,2,1,'no','yes','yes','yes',5,2,3,1,2,4,0,55,50,50),
('MS','F',18,4,4,3,2,'no','no','yes','yes',3,2,2,4,2,5,10,70,60,55),
('MS','F',19,3,2,2,2,'yes','yes','yes','yes',3,2,2,1,1,3,4,35,35,45),
('MS','M',18,1,2,3,1,'yes','yes','no','yes',4,3,3,2,3,3,3,70,60,60),
('MS','F',17,2,2,1,3,'yes','yes','yes','yes',3,4,3,1,1,3,8,65,55,55),
('MS','F',17,1,2,1,1,'yes','yes','yes','no',3,5,5,1,3,1,14,30,25,25),
('MS','F',18,4,4,2,3,'no','yes','yes','no',5,4,4,1,1,1,0,95,90,95),
('MS','F',18,1,1,4,3,'no','yes','yes','no',4,3,2,1,2,4,2,40,40,50),
('MS','F',20,4,2,2,3,'no','no','yes','yes',5,4,3,1,1,3,4,75,70,75),
('MS','F',18,4,4,1,2,'yes','yes','yes','no',5,4,3,3,4,2,4,40,45,50),
('MS','F',18,3,3,1,2,'no','yes','yes','yes',4,1,3,1,2,1,0,75,75,75),
('MS','F',17,3,1,1,2,'yes','no','yes','no',4,5,4,2,3,1,17,50,50,50),
('MS','M',18,4,4,1,2,'yes','no','yes','no',3,2,4,1,4,2,4,75,70,70),
('MS','M',18,2,1,2,1,'yes','no','yes','yes',4,4,3,1,3,5,5,35,30,35),
('MS','M',17,2,3,2,2,'yes','yes','yes','no',4,4,3,1,1,3,2,55,55,50),
('MS','M',19,1,1,2,1,'no','yes','yes','no',4,3,2,1,3,5,0,30,25,0),
('MS','M',18,4,2,2,1,'no','yes','yes','no',5,4,3,4,3,3,14,30,25,25),
('MS','F',18,2,2,2,3,'no','yes','yes','no',5,3,3,1,3,4,2,50,45,50),
('MS','F',18,4,4,3,1,'yes','yes','yes','yes',4,4,3,2,2,5,7,30,25,30),
('MS','F',19,2,3,1,3,'yes','no','yes','no',5,4,2,1,2,5,0,35,25,0),
('MS','F',18,3,1,1,2,'no','yes','yes','no',4,3,4,1,1,1,0,35,45,40),
('MS','F',18,1,1,2,2,'yes','yes','yes','no',1,1,1,1,1,5,0,30,25,0),
('MS','M',20,2,2,1,2,'no','yes','yes','no',5,5,4,4,5,4,11,45,45,45),
('MS','M',17,3,1,2,1,'no','no','yes','no',2,4,5,3,4,2,3,70,80,80),
('MS','M',21,1,1,1,1,'no','no','yes','no',5,5,3,3,3,3,3,50,40,35),
('MS','M',18,3,2,3,1,'no','no','yes','no',4,4,1,3,4,5,0,55,60,50),
('MS','M',19,1,1,1,1,'no','yes','yes','no',3,2,3,3,3,5,5,40,45,45)]


def descriptive_stats(results):
    '''Shows the mean, median, and standard deviation of a data set and 
    also gives the percentage of points falling one and two
    std deviations about the mean.'''
    mean = stats.mean(results)
    std = stats.stdev(results)
    print(f"Mean:         {mean:.2f}")
    print(f"Median:       {stats.median(results):.2f}")
    print(f"Std Dev:      {std:.2f}")
    
    interval1 = (mean - std, mean + std)
    interval2 = (mean - 2 * std, mean + 2 * std)
  
    #Find the % of all points in interval1
    dataIn1 = [point for point in results if interval1[0] <= point <=  interval1[1]]
    percentIn1 = len(dataIn1)*100/len(results)

    #Do it again for interval2
    dataIn2 = [point for point in results if interval2[0] <= point <=  interval2[1]]
    percentIn2 = len(dataIn2)*100/len(results)
    print(f"Size: {len(results)}")
    print(f"1st Interval: ({interval1[0]:.2f}, {interval1[1]:.2f}): {percentIn1:.2f}%")
    print(f"2nd Interval: ({interval2[0]:.2f}, {interval2[1]:.2f}): {percentIn2:.2f}%\n\n\n\n")
    
    
def create_freq_barchart(results, title = None, x_title = None, y_title = None, colors = None,
                  categories = None, showFreqs = False):
    
    '''Draws a barchart.'''
    
    values, frequencies = np.unique(results, return_counts = True)
    
    values = list(values)
            
    sns.set_style('whitegrid') #white background with lines for magnitude values
    
    axes = sns.barplot(x = values, y = frequencies, palette = colors, order = categories)
    axes.set_title(title) #Don't need output but has interesting info
    
    axes.set(xLabel = x_title, yLabel = y_title) #Don't need output but has interesting info

    axes.set_ylim(top=max(frequencies) * 1.10)
    if showFreqs: 
        for bar, frequency in  zip(axes.patches, frequencies):
            text_x = bar.get_x() + bar.get_width()/2
            text_y = bar.get_height()
            text = f'{frequency:,}\n{frequency/len(results):.3%}'
            axes.text(text_x, text_y, text, fontsize=11, ha='center', va = 'bottom')
        
    plt.show()
    plt.close()

if __name__ == "__main__":
      
    #So that categories 0-100 always appear
    gradeCategories = list(range(0,105,5))        

    #Task 1: Distribution of All Categories
    schools0s = school
    schools = [student for student in school if student[20] > 0]
    grades =  [student[20] for student in school if student[20] > 0]

    create_freq_barchart (results = grades, 
                        title = 'Grades for All Students', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories)

    descriptive_stats(grades)

    #From now on, we only consider....

    #Task 2:  GP vs MS
    gp_grades =  [student[20] for student in schools if student[0] == "GP"]
    ms_grades =  [student[20] for student in schools if student[0] != "GP"]

    create_freq_barchart (results = gp_grades, 
                        title = 'Grades for All GP Students', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories)

    descriptive_stats(gp_grades)

    create_freq_barchart (results = ms_grades, 
                        title = 'Grades for All ms Students', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories)

    descriptive_stats(ms_grades)

    #Task 3: Activities vs. No Activities - Appears to be a difference?
    activity_or_not = [student[7] for student in school]
    activity_grades =  [student[20] for student in schools if student[7] == "yes"]
    no_activity_grades =  [student[20] for student in schools if student[7] != "yes"]

    create_freq_barchart (results = activity_or_not, 
                        title = 'Activity Dis', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        )

    create_freq_barchart (results = activity_grades, 
                        title = 'Grades for All Activity Students', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories)

    descriptive_stats(activity_grades)

    create_freq_barchart (results = no_activity_grades, 
                        title = 'Grades for All Activity Students', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories)

    descriptive_stats(no_activity_grades)

    #Task 4: Low Absence vs. High Abscense Scores - Appears to be a difference?
    absences = [student[17] for student in schools]

    create_freq_barchart (results = absences, 
                        title = 'Attendence', 
                        x_title = "Num Abseences", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        )

    high_attendence_grades =  [student[20] for student in schools if student[17] < 15]
    low_attendence_grades =  [student[20] for student in schools if student[17] > 15]

    create_freq_barchart (results = low_attendence_grades, 
                        title = 'Low Attendence Grades', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories
                        )
    
    descriptive_stats(low_attendence_grades)

    create_freq_barchart (results = high_attendence_grades, 
                        title = 'High Attendence Grades', 
                        x_title = "Grades", 
                        y_title = "Frequency", 
                        showFreqs = False,
                        categories = gradeCategories
                        )
    
    descriptive_stats(low_attendence_grades)
