import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


df = pd.read_excel('D:/Mall_Customers.xlsx')
print(df.head())

# Features

X =df[['Annual Income (k$)','Spending Score (1-100)']]

# Visualize the data
plt.figure(figsize=(10,6))
plt.scatter(X['Annual Income (k$)'],X['Spending Score (1-100)'])
plt.title("Customer data before clustering")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()

# Normalization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

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
plt.ylabel("Intertias")
plt.show()  

# Select the value of K =5
kmeans = KMeans(n_clusters=5,n_init=10,random_state=42)
cluster = kmeans.fit_predict(X_scaled)

df['Cluster']=cluster 

print(df.head())
scatter =plt.scatter( df['Annual Income (k$)'],df['Spending Score (1-100)'],c=df['Cluster'])

# plot the Centroids
centroid = scaler.inverse_transform(kmeans.cluster_centers_)

plt.figure(figsize=(10,7))

plt.scatter(centroid[:,0],centroid[:,1],s=200,c='red',marker='X',label='Centroids')
plt.xlabel("Annual Income")
plt.ylabel("Spending score")
plt.title("Customer data -KMeans Cluserting")
plt.legend()
plt.show()

# Metrics
print("inertia value is:")
print(kmeans.inertia_)

# Silhoutte score
ss_score = silhouette_score(X_scaled,cluster,metric='euclidean') # Mean distance sample and all the other points in the same class.
print(round(ss_score,2))

# Cluster summary
summary = df.groupby('Cluster')[['Annual Income (k$)','Spending Score (1-100)']].mean()
print("Cluster summary is:",summary)