import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Data Creation
n_customers =500

income = np.random.normal(100000,1500000,n_customers)
credit_limit = income*0.25 +np.random.normal(10,5000,n_customers)
savings_balance = income *0.40+np.random.normal(10,5000,n_customers)
loan_amount = income*0.35 +np.random.normal(15,3500,n_customers)
online_purchases = np.random.normal(50,5,n_customers)
total_transactions= online_purchases*6+np.random.normal(5,20,n_customers)
emi_usage = loan_amount*0.20+np.random.normal(10,1000,n_customers)
age =np.random.randint(18,70,n_customers)
credit_utilization = credit_limit*0.8+np.random.normal(10,3000,n_customers)

# create the dataframe
df01 = pd.DataFrame(
     {
       "Age":age,
       "Income":income,
       "credit_limit":credit_limit,
       "savings_balance":savings_balance,  
       "loan_amount":loan_amount,
       "online_purchases":online_purchases,
       "total_transactions":total_transactions,
       "emi_usage":emi_usage,
       "credit_utilization":credit_utilization
     }
)

print(df01.head())

# Normalization
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df01)

# Apply PCA
pca= PCA()
pca_data = pca.fit_transform(scaled_data)

# Explained variance
explained_ratio = pca.explained_variance_ratio_
print(explained_ratio)

# cumulative explained variance
cumulative_variance = np.cumsum(explained_ratio)
print(cumulative_variance)

# visualizing the PCA
plt.figure(figsize=(10,6))

plt.plot(range(1,len(cumulative_variance)+1),cumulative_variance,marker='o')
plt.xlabel("Number of Principal Components")
plt.ylabel("Cumulative explained variance")
plt.title("Explained variance using PCA")
plt.show()

# Choosing optimal Components
pca_final = PCA(n_components=0.85)
reduced_data = pca_final.fit_transform(scaled_data)

# shape of original & reduced data
print(pca_data.shape)
print(reduced_data.shape)

print(pca_final.n_components_)

# Creating the datafrome for this PCA components
pca_columns =[]

for i in range(pca_final.n_components_):
    pca_columns.append(f'PC{i+1}')   # PC1 ,PC2

pca_df = pd.DataFrame(reduced_data,columns=pca_columns)   

print("\n Transformed Data is:")
print(pca_df.head())

# Visualize 
plt.figure(figsize=(10,6))

plt.scatter(pca_df['PC1'],pca_df['PC2'])
plt.xlabel("Principal Components 1")
plt.ylabel("Principal Components 2")
plt.title("Customer Distribution after PCA")
plt.show()

