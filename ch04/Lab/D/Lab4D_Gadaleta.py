"""
Lab4D_Gadaleta.py
Following the given instructions
author: Jake Gadaleta
"""
import statistics as stats
def basicStats(data, pritable = True):
    """Calcultes, prints, and returns the max,min, mean, meduab and sd of a list"""
    if pritable:
        print(f"""
        max:\t{max(data)}
        min:\t{min(data)}
        mean:\t{stats.mean(data)}
        median:\t{stats.median(data)}
        Pop SD:\t{stats.pstdev(data)}
        Samp SF:\t{stats.stdev(data)}
        """)

    return (
        max(data),
        min(data),
        stats.mean(data),
        stats.median(data),
        stats.pstdev(data),
        stats.stdev(data)
    )

def printIntervals(data, isApproxNormal=False):

    tuple = basicStats(data, pritable=False)

    std = tuple[len(tuple) - 1]
    mean = tuple[2]


    if  not isApproxNormal:
        x = [">=0%", ">=75%", ">=88.89%"]
    else:
        x = ["~68", "~95", "~99.7"]
    
    count = 0
    print("Combined Deviations")
    for i in range(3):
        neg = mean + (std * -i -1)
        pos = (mean + (std * (i + 1)))

        for h in data:
            if h > neg and h < pos:
                count += 1

    
        print(f"Values Between {neg:.2f} and {pos:.2f} corresponding percentage {x[i]} actual percentage {count / len(data):.2f}")
        count = 0


    counter = 0
    for i in data:
        if i > (mean + (std * 3)) or i < (mean + (std * -3)):
            counter += 1
    
    print(f"Actual percentage outside of the 3 devations: {counter / len(data):.2f}")

def zscore(value, mean, std):
    return (value - mean) / std

dailyChanges = [1, -4, 5, -8, -3, 14, -13, 8, 4, -4, -9, -11, -3, 11, -9, 5, -11, 7, 5, -15, 6, 11, -12, -2, 0, -4, 5, 3, 2, 11, 5, -1, 5, 3, -1, 2, -3, 0, 1, -7, -11, 0, 7, 0, -4, -5, 12, -1, 3, 2, -1, -2, 2, -10, -10, 8, 7, -6, -9, -1, 1, 10, -5, 4, 5, 1, -10, -3, -2, 5, 1, -4, 1, 1, 3, 9, 6, -1, -8, 5, -27, 10, -1, -8, -3, -5, 6, 14, 13, -25, -8, -3, 14, 2, 7, -3, 4, 1, -10, 4, 7, -5, -7, -1, -2, -7, -5, 3, 16, 8, -2, -14, -2, 7, -4, -4, 12, 0, -10, -5, -2, 1, -6, -9, 14, 0, 1, -5, -9, -3, 8, -2, 17, -4, -4, 0, -2, -16, 8, 6, -10, -1, 13, 0, -6, 3, 11, -14, -6, -3]

stat = basicStats(dailyChanges)
printIntervals(dailyChanges, isApproxNormal=False)


# max(data),
# min(data),
# stats.mean(data),
# stats.median(data),
# stats.pstdev(data),
# stats.stdev(data)

print(f"""
Z-Score(-25), {zscore(-25, stat[2], stat[5])}
Z-Score(-27), {zscore(-27, stat[2], stat[5])}
""")

dailyChangesTrimmed = [1, -4, 5, -8, -3, 14, -13, 8, 4, -4, -9, -11, -3, 11, -9, 5, -11, 7, 5, -15, 6, 11, -12, -2, 0, -4, 5, 3, 2, 11, 5, -1, 5, 3, -1, 2, -3, 0, 1, -7, -11, 0, 7, 0, -4, -5, 12, -1, 3, 2, -1, -2, 2, -10, -10, 8, 7, -6, -9, -1, 1, 10, -5, 4, 5, 1, -10, -3, -2, 5, 1, -4, 1, 1, 3, 9, 6, -1, -8, 5, 10, -1, -8, -3, -5, 6, 14, 13, -8, -3, 14, 2, 7, -3, 4, 1, -10, 4, 7, -5, -7, -1, -2, -7, -5, 3, 16, 8, -2, -14, -2, 7, -4, -4, 12, 0, -10, -5, -2, 1, -6, -9, 14, 0, 1, -5, -9, -3, 8, -2, 17, -4, -4, 0, -2, -16, 8, 6, -10, -1, 13, 0, -6, 3, 11, -14, -6, -3]

# DR. Ryan after this point it may help you not to read the comments I am running only linux atm and that means I can't edit your PDFs so my answers are embeded

# # 10 higher, lower
stat = basicStats(dailyChangesTrimmed)
printIntervals(dailyChanges, isApproxNormal=True)

# #11
# Values Between -1.39 and 7.26 corresponding percentage ~68 actual percentage 0.41
# Values Between -9.05 and 14.91 corresponding percentage ~95 actual percentage 0.87
# Values Between -16.70 and 22.57 corresponding percentage ~99.7 actual percentage 0.99
# Percentage outside of the 3 devations: 0.01

# # 12
#  -9.05, 14.91

# # # 13
# Hi Chrisitna,
# I hope this letter finds you well,
# moving into Octobers future we belive that the temperature can fluctatre -9° and +15°

