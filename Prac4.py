import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv('student-data.csv')

#print(df['passed'].value_counts())

#print(df.groupby('passed')['absences'].mean())

#print(df[(df['passed'] == 'yes') & (df['age'] < 20)])

#print(df[df['passed'] == 'no'][['studytime','absences']].mean())

#print(df[['studytime','absences']].mean())