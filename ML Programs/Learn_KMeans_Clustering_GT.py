import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import silhouette_score,adjusted_rand_score,normalized_mutual_info_score,confusion_matrix
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\Users\swami\Downloads\customer_segmentation_gt_5000.csv')
print(df.head())

# Separate features and Target
y_true =df['Segmentation']
X= df.drop(['ID','Segmentation'],axis =1)

#print(df.dtypes)

# Encode the categoical Variables
categorical_columns = X.select_dtypes(include='object').columns
print("\n Categorical Columns:")
print(categorical_columns)

encoders ={}

for col in categorical_columns:
   
    encoder = LabelEncoder()
    X[col]=encoder.fit_transform(X[col].astype(str))

    encoders[col]=encoder

    target_encoder = LabelEncoder()
    y_true_encoded = target_encoder.fit_transform(y_true)

# Feature Scaling
scaler  = StandardScaler()   
X_scaled = scaler.fit_transform(X)

# Elbow Method

interia=[]
for i in range(1,11):
    model = KMeans(n_clusters=i,n_init=10,random_state=42)
    model.fit(X_scaled) 
    interia.append(model.inertia_)    

# plotting Elbow Curve
plt.figure(figsize=(8,6))
plt.plot(range(1,11),interia,marker='o')
plt.title('Elbow Method')
plt.xlabel('No of Clusters')
plt.ylabel("Intertias")
plt.show()  

# Finalize the Model

kmeans = KMeans(n_clusters=4,n_init=10,random_state=42)
y_pred =kmeans.fit_predict(X_scaled)
df['Cluster'] =y_pred

print(df.head())

# Metrics
print(round(kmeans.inertia_,2))

ss_score = silhouette_score(X_scaled,y_pred)
print(round(ss_score,2))

ars_score = adjusted_rand_score(y_true_encoded,y_pred)  # 1 - accurate match  0 - No match
print(round(ars_score,2))

nmi_score = normalized_mutual_info_score(y_true_encoded,y_pred) # 1 - actual labels = predicted cluster  0- actual labels != predicted cluster
print(round(nmi_score,2))
 
#confusion Matrix
result = confusion_matrix(y_true_encoded,y_pred)

sns.heatmap(result,annot=True,fmt='g',
            xticklabels=['Cluster 0','Cluster 1','Cluster 2','Cluster 3'],
            yticklabels=['Segement A','Segment B','Segment C','Segment D'])

plt.xlabel('Prediction',fontsize=12)
plt.ylabel('Actual',fontsize=12)
plt.title('Confusion Matrix',fontsize=14)
plt.show()

# Business Visualization
plt.figure(figsize=(8,6))

plt.scatter(df['Annual_Income'],df['Spending_Score'],c=df['Cluster'],s=500)

# plot the Centroids
centroid = scaler.inverse_transform(kmeans.cluster_centers_)

income = X.columns.get_loc('Annual_Income')
spend = X.columns.get_loc('Spending_Score')

plt.scatter(centroid[:,income],centroid[:,spend],s=500,c='red',marker='X',label='Centroids')
plt.xlabel("Annual Income")
plt.ylabel("Spending score")
plt.title("Customer segementation with GT")
plt.legend()
plt.show()

# Cluster summary
summary = df.groupby('Cluster')[['Age','Spending_Score','Family_Size','Annual_Income']].mean()
print("Cluster summary is:",summary)