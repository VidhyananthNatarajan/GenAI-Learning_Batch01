import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read & Load the data
df01 = pd.read_csv("D:\Data Analyst\diabetes.csv")
print(df01)

# data strcuture and missing values

print(df01.info())

print(df01.isnull().sum())

# statistical measures

print(df01.describe())

#Outliers removal

q1,q3 =np.percentile(df01['Insulin'],[25,75])
iqr = q3-q1
lower_bound=q1-1.5*iqr
higher_bound=q3+1.5*iqr
df01_updated = df01[(df01['Insulin'] >lower_bound) & (df01['Insulin'] >higher_bound)]
print(df01_updated)

# Visualize Target variable
plt.pie(df01['Outcome'].value_counts(),labels=['Diabetic','Non-Diabetic'],autopct='%.f%%')
plt.title("Diabetic Outcome")
plt.show()