#HW 5D
# Jake Gadaleta

import statistics as stat

def printNicely(interval, percent):
    """Prints an interval and a percent nicely"""
    print(f'The exact perecentage of data in ({interval[0]:.2f}, {interval[1]:.2f}) is {percent:.2f}%')
    
data = [1, -4, 5, -8, -3, 14, -13, 8, 4, -4, -9, -11, -3, 11, -9, 5,
                -11, 7, 5, -15, 6, 11, -12, -2, 0, -4, 5, 3, 2, 11, 5, -1, 5,
                3, -1, 2, -3, 0, 1, -7, -11, 0, 7, 0, -4, -5, 12, -1, 3, 2,
                -1, -2, 2, -10, -10, 8, 7, -6, -9, -1, 1, 10, -5, 4, 5, 1,
                -10, -3, -2, 5, 1, -4, 1, 1, 3, 9, 6, -1, -8, 5, -27, 10, -1,
                -8, -3, -5, 6, 14, 13, -25, -8, -3, 14, 2, 7, -3, 4, 1, -10,
                4, 7, -5, -7, -1, -2, -7, -5, 3, 16, 8, -2, -14, -2, 7, -4,
                -4, 12, 0, -10, -5, -2, 1, -6, -9, 14, 0, 1, -5, -9, -3, 8,
                -2, 17, -4, -4, 0, -2, -16, 8, 6, -10, -1, 13, 0, -6, 3, 11,
                -14, -6, -3]

mean =  stat.mean(data)
stdDev = stat.stdev(data)
  
interval1 = (mean - stdDev, mean + stdDev)
interval2 = (mean - 2 * stdDev, mean + 2 * stdDev)
interval3 = (mean - 3 * stdDev, mean + 3 * stdDev)
  
#Get a list of items in interval1, that is, if interval1 is -8 to 7, get
#a filtered down list with only those points between -8 and 7.
#Use a list comprehension so fill in the blank below!
dataIn1 = [point for point in data if point > interval1[0] and point < interval1[1]]

#Find the % of all points in interval1
percentIn1 = len(dataIn1)/len(data)

#print the details out nicely
printNicely(interval1, percentIn1)

#Do it again for interval2
dataIn2 = [point for point in data if point > interval2[0] and point < interval2[1]]
percentIn2 = len(dataIn2)/len(data)
printNicely(interval2, percentIn2)


#Do it again for interval3
dataIn3 = [point for point in data if point > interval3[0] and point < interval3[1]]
percentIn3 = len(dataIn3)/len(data)
printNicely(interval3, percentIn3)

