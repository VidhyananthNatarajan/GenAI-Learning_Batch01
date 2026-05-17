# Marks scored by 20 students in two subjects x & y
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

x=[5,4,13,11,15,5,9,8,10,12,13,14,19,20,21,17,16,9,18,24]
y=[15,18,22,21,20,18,19,16,16,10,11,15,12,13,9,8,6,24,23,25]

plt.scatter(x,y,color='black')
plt.show()

# Combine the data scores of students in 2 subjects and see who is under performing

data =list(zip(x,y))
print(data)

#KMeans Clustering
kmeans = KMeans(n_clusters=4,n_init='auto')
kmeans.fit(data)
c=kmeans.labels_
print(c)

# Display the clusters
plt.scatter(x,y,c=kmeans.labels_)
plt.show()

# Elbow Method
# inertias - sum of squared errors or distance within the cluster (sum of squared errors)
list_inertias=[]
data =list(zip(x,y))
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,n_init='auto')
    kmeans.fit(data)
    list_inertias.append(kmeans.inertia_)
print(list_inertias) 


# Elbow Plot
plt.plot(range(1,11),list_inertias,marker='o')
plt.title('Elbow Method')
plt.xlabel('No of Clusters')
plt.ylabel("SSE")
plt.show()

# Silhoutte Score
ss_score =silhouette_score(data,c,metric='euclidean')
print(ss_score)