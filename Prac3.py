import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student-data.csv')

print(df.groupby('passed')['traveltime'].mean())

print(df.groupby('passed')['Dalc'].mean())


print(df.groupby('passed')['absences'].mean())
df.groupby('passed')['absences'].mean().plot(kind='bar')
plt.title('Average Absences by Pass/Fail')
plt.show()

print(df.groupby('internet')['passed'].value_counts())
df.groupby('internet')['passed'].value_counts().plot(kind='bar')
plt.xlabel('Internet Access')
plt.title('Pass/Fail by Internet Access')
plt.show()


