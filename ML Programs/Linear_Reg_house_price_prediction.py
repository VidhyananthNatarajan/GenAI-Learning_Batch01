import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,root_mean_squared_error


df01 = pd.read_csv("D:\housing_price_details.csv")
print(df01)

# split the features (Input) & target

X=df01[["area","bedrooms","building_age"]]
y=df01["price"]

# Splitting of Training & testing data

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42) 

# training the dataset
model = LinearRegression()
model.fit(X_train,y_train)

# prediction
y_pred = model.predict(X_test)

print("Actual values:",y_test.round(2).tolist())
print("Predicted values",y_pred.round(2).tolist())



#Evaluation Metrics
mse = mean_squared_error(y_test,y_pred)
#rmse = np.sqrt(mse)

rmse = root_mean_squared_error(y_test,y_pred)

print("Mean Squared Error is:",mse)
print("Root Mean Squared Error is:",rmse)