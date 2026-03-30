import pandas as pd

df = pd.read_csv('student_data_1.csv')

#case concept----------------------------------------------------------------------------------------------------------------------

#df['absence_category'] = pd.cut(
#    df['absences'],
#    bins=[-float('inf'), 5, 10, float('inf')],
#    labels=['Low', 'Medium', 'High']
#)

#def absence_count(x):
#    if x <= 5:
#        return 'Low'
#    elif x <= 10:
#        return 'Medium'
#    else:
#        return 'High'
#
#df['absence_category'] = df['absences'].apply(absence_count)

#df['absence_category'] = df['absences'].apply(lambda x: 'Low' if x <= 5 else ('Medium' if x <= 10 else 'High'))

#print(df[['absences', 'absence_category']])


#--condition first result later--------------------------------------------------------------------------------------------------------------

#print(df[df['absences'] > 6].groupby('passed')['absences'].mean())


#---Having--------------------------------------------------------------------------------------------------------------

#avg_absences = df.groupby('passed')['absences'].mean()
#result = avg_absences[avg_absences > 6]
#print(result)

#-- subquery select * from table where absences > avg_abs

#avg_abs= df['absences'].mean()
#print(df[df['absences']> avg_abs])

#----------std with > abg_absences and < avg_studyTime--------------------------------------------------------------------------------------

#avg_stdtime= df['studytime'].mean()
#avg_abs= df['absences'].mean()
#print(df[(df['absences'] > avg_abs) & (df['studytime'] < avg_stdtime)])

#print(len(df[(df['absences'] > avg_abs) & (df['studytime'] < avg_stdtime)]))