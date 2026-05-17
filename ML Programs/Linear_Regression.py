import pandas as pd
import matplotlib.pyplot as plt

from sklearn import linear_model

#from scikit-learn import linear_model
from sklearn.model_selection import train_test_split

# Load the dataset

df01 = pd.read_csv("D:\Data Analyst\Housing.csv")
print(df01)

# Lot size -> input variable, Price -> output variable

X=df01['lotsize']
Y=df01['price']

X=X.to_numpy().reshape(len(X),1)
Y=Y.to_numpy().reshape(len(Y),1)

# Splitting of Training & testing data

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42) 

# Select the alogorithm

regr = linear_model.LinearRegression()

# Train the algorithm
regr.fit(X_train,Y_train)

y_test =regr.predict(X_test)

plt.scatter(X_test,Y_test, color='black')
plt.title("House Rate Prediction")
plt.xlabel("size")
plt.ylabel("price")


plt.plot(X_test,y_test,color='blue',linewidth=2.5)
plt.show()

