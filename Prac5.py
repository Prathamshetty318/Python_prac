import pandas as pd
import matplotlib.pyplot as plt

df1= pd.read_csv('student_data_1.csv')
df2= pd.read_csv('student_data_2.csv')


df1= df1[['student_id','age','passed']]
df2= df2[['student_id','studytime']]

df_final = df1.merge(df2, on='student_id')

print(df_final)


