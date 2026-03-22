import pandas as pd

df = pd.read_csv('student-data.csv')

#print(df.describe())

#print(df.head())

#print(df.tail())

#print(df.info())

#print(df["age"])

#print(df[["age","sex","address"]])

print (df[df["age"]<20])