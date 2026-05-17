import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#Load the dataset

df01 = pd.read_csv("D:\Data Analyst\Titanic-Dataset.csv")
print(df01)

# Summaries & Profiling the data
print(df01.info())

# head & tail
print(df01.head(6))
print(df01.tail(10))

#Identify column types
category_col = [col for col in df01.columns if df01[col].dtype =='object']

numerical_col = [col for col in df01.columns if df01[col].dtype!='object']

print("Categorical columns are:",category_col)
print("Numerical columns are:",numerical_col)

# Unique values
print(df01[category_col].nunique())

# Missing values
print(df01.isnull().sum())

# dropping some columns
df02 =df01.drop(columns=['Name','Cabin','Ticket'])
print(df02)

df02['Age'] =df01['Age'].fillna(df01['Age'].mean())
print(df02)

print(df02.isnull().sum())

print(df02.describe())
print(df02.info())