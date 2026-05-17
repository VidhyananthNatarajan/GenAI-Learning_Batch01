import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
import seaborn as sns

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

headernames =['sepal-length','sepal-width','petal-length','petal-width','Class']

data = pd.read_csv(path,names=headernames)
print(data)

# Extract the features and the output class
X=data.iloc[:,:-1].values # Extract only the input features
y=data.iloc[:,4].values  # extract only the class

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.30,random_state=12)

# Classification - Data preprocessing
scaler = StandardScaler()
scaler.fit(X_train) # scaler.fit is used for normalizing the value/data and to calculate the mean & SD
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)

# Gaussian NB
classifier = GaussianNB()
classifier.fit(X_train,y_train)

# Predict the model using the training data set

y_pred_train =classifier.predict(X_train)

# Calculate the accuracy of training data set
accuracy = accuracy_score(y_train,y_pred_train)
print("Accuracy of the training data set  is:",round(accuracy,2))

# Predict the model using the testing data set

y_pred_test =classifier.predict(X_test)

# Calculate the accuracy of testing data set
accuracy = accuracy_score(y_test,y_pred_test)
print("Accuracy of the testing data set is:",round(accuracy,2))

# Creating the Confusion Matrix

result = confusion_matrix(y_test,y_pred_test)

sns.heatmap(result,annot=True,fmt='g',
            xticklabels=['setosa','versicolor','virginica'],
            yticklabels=['setosa','versicolor','virginica'])

plt.xlabel('Prediction',fontsize=12)
plt.ylabel('Actual',fontsize=12)
plt.title('Confusion Matrix',fontsize=14)
plt.show()


# Classification Report

classi_report = classification_report(y_test,y_pred_test)
print(classi_report)