import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student-data.csv")

#df['passed'].value_counts().plot(kind="bar")
#plt.title("Passed vs Failed")
#plt.show()

#df.groupby('romantic')['absences'].mean().plot(kind='bar')
#plt.title("Avg Absence by romantic relationship")
#plt.show()

#df.groupby('passed')['studytime'].mean().plot(kind='bar')
#plt.title("Avg Study Time by pass/fail")
#plt.show()

ax = df.groupby('passed')['absences'].mean().plot(kind="bar")
plt.title("Avg Absence by pass/fail ")
plt.xlabel("Results")
plt.ylabel("Avg Absences")

plt.xticks(rotation=0)

for i,v in enumerate(df.groupby("passed")["absences"].mean()):
    ax.text(i,v + 0.1,round (v,2), ha='center')
    
plt.show()