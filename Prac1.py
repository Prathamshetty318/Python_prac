import pandas as pd

df = pd.read_csv("student-data.csv")

#print(f"Rows found:{len(df)}")

#print(df.describe())

#print(df.head())

#print(df.tail())

#print(df.info())

#print(df["age"])

#print(df[["age","sex","address"]])

#print (df[df["age"]<20])


#print(df[(df["age"] > 20) & (df["sex"] == "M")])

#print(df[df["age"]<20])

#print (df["sex"].value_counts())

#print(df[(df["age"] < 20) & (df["passed"] == "yes")])

#print(df["passed"].value_counts())

#print(df["studytime"].mean())

#print(df.groupby("sex")["studytime"].mean())


#print(df.groupby('passed')["Walc"].mean())

#print(df.groupby("passed")["studytime"].mean())

#print(df.groupby("passed")["absences"].mean())

#print(df.groupby(["sex","passed"])["studytime"].mean())

print(df.groupby("romantic")["absences"].mean())
print(df.groupby("Fjob")["absences"].mean())
print(df.groupby("Mjob")["absences"].mean())