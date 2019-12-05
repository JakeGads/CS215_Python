import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('complaints.csv')

print(df.columns)
print(df.ndim)
print(df.shape)

# complaints per hour
# 'num_visits', 'num_complaints', 'residency', 'gender', 'revenue', 'hrs'
df['complaints_per_1000hour'] = (df['num_complaints'] / df['hrs']) * 1_000
print(df)

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
filed = females.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
plt.title("Number of Complaints Against Female Physicians")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 19, 2))
plt.xticks((range(0, 8)))
plt.show()


criteria = df["gender"] != 'F'
males = df[criteria]
filed = males.sort_values(by='complaints_per_1000hour', ascending=False).loc[:, "complaints_per_1000hour"]

histo = filed.hist(grid=True, bins=xBins)
plt.title("Number of Complaints Against Male Physicians")
plt.ylabel("Frequency")
plt.xlabel("Number of complaints (Per 1000 hours)")
plt.yticks(range(0, 19, 2))
plt.xticks((range(0, 8)))
plt.show()
