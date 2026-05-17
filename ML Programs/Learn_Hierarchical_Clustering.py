import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
from scipy.cluster.hierarchy import fcluster
from sklearn import metrics

# Marks scored by 25 students in 2 subjects

x=[5,4,13,11,13,5,3,4,3,10,12,13,14,12,11,6,8,7,15,11,14,10,12,13,14]
y=[15,18,22,19,21,16,16,21,23,20,17,9,18,16,10,14,11,19,17,9,18,21,15,11,14]

plt.scatter(x,y,color ='black')
plt.show()

data = list(zip(x,y))
print(data)

#Min Linkage - Method - Single
HC01 = linkage(data,method='single',metric='euclidean')

#Max Linkage - Method - Complete
HC02 = linkage(data,method='complete',metric='euclidean')

#Averge Linkage - Method - average
HC03 = linkage(data,method='average',metric='euclidean')

#Ward Linkage - Method - Ward
HC04 = linkage(data,method='ward',metric='euclidean')

#Max Linkage - Method - centtroid
HC05 = linkage(data,method='centroid',metric='euclidean')

# Finding the optimal number of clusters
c= fcluster(HC02,3,criterion='maxclust')
print(f"No of clusters are: {c}")

# Dendogram 
plt.plot(2,2,1),dendrogram(HC04),plt.title('Ward')
plt.show()

# silhoutte score
ss_score = metrics.silhouette_score(data,c,metric='euclidean')
print(ss_score)