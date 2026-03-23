import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student-data.csv")

#df['passed'].value_counts().plot(kind="bar")
#plt.title("Passed vs Failed")
#plt.show()

#df.groupby('passed')['absences'].mean().plot(kind="bar")
#plt.title("Avg Absence by pass/fail ")
#plt.show()

#df.groupby('romantic')['absences'].mean().plot(kind='bar')
#plt.title("Avg Absence by romantic relationship")
#plt.show()