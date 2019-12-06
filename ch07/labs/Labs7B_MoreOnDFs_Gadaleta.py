import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


def descriptive_stats(df: pd.core.frame.DataFrame, loc='complaints_per_1000hour'):

    return f"""
    Mean:       {df[loc].mean()}
    Median:     {df[loc].median()}
    Min:        {df[loc].min()}
    Max:        {df[loc].max()}
    STD:       {df[loc].std()}
    """

df = pd.read_csv('complaints.csv')

print(df.columns)
print(df.ndim)
print(df.shape)

# complaints per hour
# 'num_visits', 'num_complaints', 'residency', 'gender', 'revenue', 'hrs'
df['complaints_per_1000hour'] = (df['num_complaints'] / df['hrs']) * 1_000


print(f"""
MAX: {df['complaints_per_1000hour'].max()}
MIN: {df['complaints_per_1000hour'].min()}
""")

xBins = np.arange(-.5, 8, 1)

filed = df.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
plt.title("Number of Complaints Against Physicians")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 19, 2))
plt.xticks((range(0, 8)))
plt.show()


criteria = df["gender"] == 'F'
females = df[criteria]
print("Female", len(females))

filed = females.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
plt.title("Number of Complaints Against Female Physicians")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 13, 2))
plt.xticks((range(0, 8)))
plt.show()


criteria = df["gender"] != 'F'
males = df[criteria]
print("Male", len(males))
filed = males.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
plt.title("Number of Complaints Against Male Physicians")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 13, 2))
plt.xticks((range(0, 8)))
plt.show()

"How do the distribution of complaints compare for residents vs. non-residents?"
criteria = df["residency"] == 'Y '
residents = df[criteria]
filed = residents.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
print("Number of Complaints Against Residents")
plt.title("Number of Complaints Against Residents")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 13, 2))
plt.xticks((range(0, 8)))
plt.show()

print(descriptive_stats(residents))

criteria = df["residency"] == 'N '
residents = df[criteria]

filed = residents.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]
histo = filed.hist(grid=True, bins=xBins)
print("Number of Complaints Against Non-Residents")
plt.title("Number of Complaints Against Non-Residents")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 13, 2))
plt.xticks((range(0, 8)))
plt.show()

"""
Calculate the descriptive stats and the histograms data for number of complaints (per 1000 hours) for the categories 
related to your problem.
"""
print(descriptive_stats(residents))

"""
Number of Complaints Against Residents  |   Number of Complaints Against Non-Residents

    Mean:       2.0125969534278783      |   Mean:       2.4543476043397985
    Median:     1.6685685657825156      |   Median:     1.706779504822756
    Min:        0.5574912891986062      |   Min:        0.0
    Max:        5.7224606580829755      |   Max:        6.597690808217124
    STD:        1.3188475659870031      |   STD:        1.8126280373428263
    
    So we can see that in general it appears that Non residents receive more complaints then residents 
"""
