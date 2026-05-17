import numpy as np
from sklearn.linear_model import LogisticRegression

# X is the input variable that is going to represent the size of the tumor

X =np.array([3.78,2.44,2.09,0.45,1.72,1.87,4.92,4.34,4.96,5.01]).reshape(-1,1)
y=np.array([0,0,0,0,0,0,1,1,1,1])

print(X)
print(y)

# Training

logr =LogisticRegression()
logr.fit(X,y)

#Prediction
Predicted_value = logr.predict(np.array([3.02]).reshape(-1,1))
print(Predicted_value)

# We predicted that tumour with the size of 3.02mm is not cancerous

def logit2prob(logr,x):
    log_odds= logr.coef_ *x+logr.intercept_    # extracting the coefficient and add with the intercept
    odds =  np.exp(log_odds)      # converting the log odds to  exponential Odds
    probability = odds/(1+odds)
    return(probability)

print(logit2prob(logr,X))

