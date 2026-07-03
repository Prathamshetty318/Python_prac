import pandas as pd

df = pd.read_csv('student_data_1.csv')

#print(df.isnull().sum())

#print(df.duplicated().sum())

#print(df.groupby("passed")["absences"].mean())
#print(df.groupby("passed")['studytime'].mean())
#print(df.groupby("passed")['Walc'].mean())
#print(df.groupby("passed")['Dalc'].mean())

#The analysis shows that absences have the strongest relationship with student performance, with a difference of approximately 1.6 between students who passed and those who failed. In contrast, factors such as study time and alcohol consumption show only minor differences, indicating a weaker relationship with performance.
#
#print(df.groupby("romantic")["absences"].mean())
#print(df.groupby("Walc")['absences'].mean())
#print(df.groupby("Dalc")['absences'].mean())
#print(df.groupby("goout")['absences'].mean())

#The analysis shows that students in romantic relationships have significantly higher absences (7.44 vs 4.84), indicating a strong relationship between relationships and absenteeism. Additionally, daily alcohol consumption (Dalc) shows a clear increasing trend with absences, suggesting that higher alcohol consumption is associated with increased absenteeism. Weekend alcohol consumption shows moderate variation, while going out frequency does not show a consistent pattern, indicating a weaker relationship.

#avg_abs = df['absences'].mean()

#avg_studytime = df['studytime'].mean()

#print(df[(df['absences']> avg_abs)&(df['studytime']<avg_studytime)&(df['passed']=='no')])

#as per the data Out of the 114 students identified with high absenteeism and low study time, 45 have already failed their exams. This group is considered high-risk, as their current habits strongly correlate with academic failure and are likely to impact their future performance. This group represents a critical segment where early intervention, such as attendance monitoring and academic support, could improve overall outcomes.

#print(df.groupby("Walc")["passed"].value_counts())
#print(df.groupby("Dalc")["passed"].value_counts())
#print(df.groupby("goout")["passed"].value_counts())

#The analysis shows that lifestyle factors such as weekend alcohol consumption and going-out frequency have a weak and inconsistent relationship with student performance. Daily alcohol consumption shows a slight decline in pass rates as consumption increases; however, the pattern is not consistent across all levels, indicating only a moderate relationship overall.

print(df.groupby("internet")["passed"].value_counts(normalize=True))

#Students with internet access have a slightly higher pass rate (68.4%) compared to those without (60.6%), indicating a mild positive relationship between internet access and performance.