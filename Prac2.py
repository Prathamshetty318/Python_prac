import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("student-data.csv")

df['passed'].value_counts().plot(kind="bar")
plt.title("Passed vs Failed")
plt.show()