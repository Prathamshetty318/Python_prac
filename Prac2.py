import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student-data.csv")

#plt.figure()
#df['passed'].value_counts().plot(kind="bar")
#plt.title("Passed vs Failed")
#plt.show()
#
#plt.figure()
#df.groupby('romantic')['absences'].mean().plot(kind='bar')
#plt.title("Avg Absence by romantic relationship")
#plt.show()

#df.groupby('passed')['studytime'].mean().plot(kind='bar')
#plt.title("Avg Study Time by pass/fail")
#plt.show()


#
#plt.figure()
#ax = df.groupby('passed')['absences'].mean().plot(kind="bar")
#plt.title("Avg Absence by pass/fail ")
#plt.xlabel("Results")
#plt.ylabel("Avg Absences")
#plt.xticks(rotation=0)
#for i,v in enumerate(df.groupby("passed")["absences"].mean()):
#    ax.text(i,v + 0.1,round (v,2), ha='center')
#    
#plt.show()


fig, axes = plt.subplots(1,3, figsize=(15,5))

df.groupby('passed')['absences'].mean().plot(kind="bar", ax=axes[0])
axes[0].set_title("Avg Absence by pass/fail")

dax = df.groupby('passed')['absences'].mean().plot(kind="bar", ax=axes[1])
axes[1].set_title("Avg Study Time by pass/fail")
axes[1].set_xlabel("Results")
axes[1].set_ylabel("Avg Absences")
for i,v in enumerate(df.groupby("passed")["absences"].mean()):
    axes[1].text(i,v + 0.1,round (v,2), ha='center')

df.groupby('romantic')['absences'].mean().plot(kind='bar', ax=axes[2])
axes[2].set_title("Avg Absence by romantic relationship")

plt.tight_layout()
plt.show()