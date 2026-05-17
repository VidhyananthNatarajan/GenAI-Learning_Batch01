from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X,y=load_breast_cancer(return_X_y=True)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42) 

logis = LogisticRegression(max_iter=950,random_state=10)
logis.fit(X_train,y_train)

# prediction
y_pred =logis.predict(X_test)
#print(y_pred)

acc=round(accuracy_score(y_test,y_pred)*100,2)
print(f"Logistics Regression Model accuracy:{acc:.2f}%")