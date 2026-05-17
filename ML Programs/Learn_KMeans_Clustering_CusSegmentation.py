# Customer segmentation - Critical features: Age,Income & Spending score -WITHOUT GT
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
OMP_NUM_THREADS=2

# Create the dataset
n_customers = 300

age =np.random.randint(18,70,n_customers)
income = np.random.randint(15000,150000,n_customers)
spending_score = np.random.randint(1,100,n_customers)

# Create the dataframe

df01 = pd.DataFrame({
  'Age':age,
  'Income':income,
  'Spending_Score':spending_score
})

print(df01.head())

# Understanding clustering using visualization:
plt.figure(figsize=(8,6))
plt.scatter(df01['Income'],df01['Spending_Score'])
plt.xlabel("Annual Income")
plt.ylabel("Spending score")
plt.title("Customer data -spend")
plt.show()

# Feature Scaling and normalization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df01)

# Find the optimal value for K using Elbow Method

list_inertias=[]

for i in range(1,11):
    model = KMeans(n_clusters=i,n_init=10,random_state=42)
    model.fit(X_scaled) 
    list_inertias.append(model.inertia_)    

# plotting Elbow Curve
plt.figure(figsize=(8,6))
plt.plot(range(1,11),list_inertias,marker='o')
plt.title('Elbow Method')
plt.xlabel('No of Clusters')
plt.ylabel("SSE")
plt.show()  

# Assume K =4
kmeans = KMeans(n_clusters=4,n_init=10,random_state=42)
clusters =kmeans.fit_predict(X_scaled)

df01['Cluster']=clusters  

print(df01.head())

scatter =plt.scatter( df01['Income'],df01['Spending_Score'],c=df01['Cluster'])

# plot the Centroids
centroid = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(centroid[:,1],centroid[:,2],s=300,c='red',marker='X',label='Centroids')
plt.xlabel("Annual Income")
plt.ylabel("Spending score")
plt.title("Customer data -KMeans Cluserting")
plt.legend()
plt.show()

# Metrics
print("inertia value is:")
print(kmeans.inertia_)

# Silhoutte score
ss_score = silhouette_score(X_scaled,clusters,metric='euclidean') # Mean distance sample and all the other points in the same class.
print(round(ss_score,2))

# Cluster summary
summary = df01.groupby('Cluster').mean()
print("Cluster summary is:",summary)