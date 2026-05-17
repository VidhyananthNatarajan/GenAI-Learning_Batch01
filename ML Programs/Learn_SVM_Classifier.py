import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
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

#SVC - Support Vector Classifier
# Kernel -> linear, poly,rbf,sigmoid
ker_list =['linear','poly','rbf','sigmoid']
accuracy_list_train=[]
accuracy_list_test=[]

print("\n The accuracy based on training data set:")

for i in ker_list:
   cal= SVC(kernel=i)
   cal.fit(X_train,y_train)
   y_pred =cal.predict(X_train)
   acc_score= accuracy_score(y_train,y_pred)
   accuracy_list_train.append(acc_score)

   print("accuracy of "+i +" is:",round(float(acc_score),2))

print("\n The accuracy based on testing data set:")

for i in ker_list:
   cal= SVC(kernel=i)
   cal.fit(X_train,y_train)
   y1_pred =cal.predict(X_test)
   acc_score= accuracy_score(y_test,y1_pred)
   accuracy_list_test.append(acc_score)

   print("accuracy of "+i +" is:",round(float(acc_score),2))

# Confusion Matrix
result = confusion_matrix(y_test,y1_pred)

sns.heatmap(result,annot=True,fmt='g',
            xticklabels=['setosa','versicolor','virginica'],
            yticklabels=['setosa','versicolor','virginica'])

plt.xlabel('Prediction',fontsize=12)
plt.ylabel('Actual',fontsize=12)
plt.title('Confusion Matrix',fontsize=14)
plt.show()   

# Classification Report
classi_report = classification_report(y_test,y1_pred)
print(classi_report)
