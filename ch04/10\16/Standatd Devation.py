import numpy

scores = [10,85,86,89,90]
sum(scores) / len(scores)

import statistics as stats

def printSD(data):
    sampleSD = stats.stdev(data)
    popSD = stats.pstdev(data)

    print(
        f"""
        Sample:\t{sampleSD}
        Population:\t{popSD}
        """
    )

dataA = [63,68,71,78,80]
dataB = [10,85,86,89,90]
dataC = [20, 70, 80, 90, 100]

data = [dataA, dataB, dataC]

for i in data:
    printSD(i)
    print("\n\n")

x = 3

def sillyMethod3():
    global x
    x = 4
    x *= 2
    print(x)

print(x)
sillyMethod3()
print(x)