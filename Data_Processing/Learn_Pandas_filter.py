import pandas as pd
import numpy as np

df01 = pd.read_csv("D:\players_22.csv")
#print(df01)

# filtering
print(df01.loc[np.logical_and(df01['nationality_name']=='Argentina',df01['club_name']=='Barcelona Sporting Club')])

# sample data creation
input_data={"Name":["user01","user02","user03","user04"],
            "favouritenumber":np.random.randint(123,234,size=(4,)),
            "randomnumber":np.random.randint(30,100,size=(4,)),
            "color":["Red","Orange","Black","Blue"]       
            }

#df02 = pd.DataFrame(input_data)
#df02.to_csv("D:\input_data.csv",index=False)

# reading from the saved location

data_df01 = pd.read_csv("D:\input_data.csv")
print(data_df01)

#Data Slicing

print(data_df01[0:2])

print(data_df01.iloc[2])

print(data_df01["Name"])

#print(data_df01[["Name","color"]])


print(data_df01[["Name","randomnumber","color"]])

# head & tail
#print(df01.head(10))

#print(df01.tail(15))

#print(df01.info())

#print(df01.describe())

# creating a new column

print(data_df01)

classname =['Sixth','Seventh','Eigth','Ninth']

data_df01["ClassName"] =classname
print(data_df01)

df01_emp =pd.read_csv("D:\Data Analyst\Employee_details.csv")
print(df01_emp)

#sorting the details
print(df01_emp.sort_values("Age"))

print(df01_emp.sort_values("Age",ascending=False))

#GroupBy operation & Agggregation

print(df01_emp.groupby("Dept")["Salary"].mean())

print(df01_emp.groupby("Dept")["Salary"].sum())

print(df01_emp.groupby("Dept")["Salary"].max())

print(df01_emp.groupby("Dept")["Salary"].count())