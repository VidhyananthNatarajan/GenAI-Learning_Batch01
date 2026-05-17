import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from  sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns

# Load the dataset
titanic_data = pd.read_csv('D:\Data Analyst\Titanic-Dataset.csv')
print(titanic_data.head())

# Dropping the missing values if exists
titanic_data =titanic_data.dropna(subset=['Survived'])

#X=titanic_data[['PassengerId','Pclass','Sex','Age','Parch','Fare']]
X=titanic_data[['Pclass','Sex','SibSp','Age','Parch','Fare']]
y=titanic_data['Survived']

X['Sex'] =X['Sex'].map({'female':0,'male':1})
X['Age'] =X['Age'].fillna(X['Age'].median())
#y['Survived']=y['Survived'].map({1:'Survived',0:'Not Survived'})

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=10)

# Train using Random Forest Model
random_classifier = RandomForestClassifier(n_estimators=50,random_state=24)
random_classifier.fit(X_train,y_train)

# Training data accuracy

y_pred_train = random_classifier.predict(X_train)
train_accuracy_score = accuracy_score(y_train,y_pred_train)
print("Accuracy of the training model is:",round(train_accuracy_score,2))

# Testing data accuracy

y_pred_test = random_classifier.predict(X_test)
test_accuracy_score = accuracy_score(y_test,y_pred_test)
print("Accuracy of the testing model is:",round(test_accuracy_score,2))

#confusion Matrix
result = confusion_matrix(y_test,y_pred_test)

sns.heatmap(result,annot=True,fmt='g',
            xticklabels=['Survived','Not Survived'],
            yticklabels=['Survived','Not Survived'])

plt.xlabel('Prediction',fontsize=12)
plt.ylabel('Actual',fontsize=12)
plt.title('Confusion Matrix',fontsize=14)
plt.show()