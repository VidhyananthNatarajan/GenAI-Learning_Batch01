import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Marks scored by the students in 2 subjects - 20 samples of data

x=[5,4,13,11,15,5,9,8,10,12,13,14,19,20,21,17,16,9,18,24]
y=[15,18,22,21,20,18,19,16,16,10,11,15,12,13,9,8,6,24,23,25]

plt.scatter(x,y,color='black')
plt.show()

data =list(zip(x,y))
print(data)

kmeans = KMeans(n_clusters=3,n_init='auto')
kmeans.fit(data)

c=kmeans.labels_
print(c)

# Plot this in the visual mode
plt.scatter(x,y,c=kmeans.labels_)
plt.show()

# Elbow Method - to find the optimal number of clusters
inertias=[]  # sum of squared errors or within cluster sum of squared errors
data =list(zip(x,y))
for i in range(1,11):
    kmeans = KMeans(n_clusters=3,n_init='auto')
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

print(inertias)  

# Plot the interias 

plt.plot(range(1,11),inertias,marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Sum of Squared Errors')
plt.show()




