#Title:ICC Test Batting Figures
#Group Member:-1.Prathmesh Lashkare_237
#              2.Jayantika Karna_229
#              3.Akash Jarad_228
#Assignment No.6

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.cluster import KMeans

data=pd.read_csv("ICC_Test1.csv",encoding= 'unicode_escape')
data1={'x':data["Runs Scored"], 'y':data["Fifties"]}
data=pd.DataFrame(data1, columns=['x','y'])

km= KMeans(n_clusters=3).fit(data)
centroids=km.cluster_centers_

plt.xlabel('Runs Scored')
plt.ylabel('Fifties')
plt.scatter(data['x'],data['y'],c=km.labels_.astype(float),s=60, alpha=1)
plt.scatter(centroids[:,0],centroids[:,1],c='red',s=190)

plt.show()

data=pd.read_csv("ICC_Test1.csv",encoding= 'unicode_escape')
df = pd.DataFrame(data)

# Selecting the features for clustering


feat= df[['Batting Average','Matches Played']]

# Specifying the number of clusters
n_clusters = 4

# Fitting the K-means model
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(feat)

# Adding the cluster labels to the DataFrame
df['Cluster'] = kmeans.labels_

# Visualizing the clusters
plt.scatter(feat['Matches Played'], feat['Batting Average'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Matches Played')
plt.ylabel('Batting Average')
plt.title('K-means Clustering')
plt.show()

data=pd.read_csv("ICC_Test1.csv",encoding= 'unicode_escape')
df = pd.DataFrame(data)

# Selecting the features for clustering


feat= df[['Fifties','Runs Scored']]

# Specifying the number of clusters
n_clusters = 4

# Fitting the K-means model
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
kmeans.fit(feat)

# Adding the cluster labels to the DataFrame
df['Cluster'] = kmeans.labels_

# Visualizing the clusters
plt.scatter(feat['Runs Scored'], feat['Fifties'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Matches Played')
plt.ylabel('Batting Average')
plt.title('K-means Clustering')
plt.show()

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


data=pd.read_csv("ICC_Test1.csv",encoding= 'unicode_escape')
x=np.array(data['Matches Played']).reshape(-1,1)
y=np.array(data['Fifties'])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
regressor= LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
x_pred=regressor.predict(x_train)

plt.scatter(x_train, y_train, color="green")
plt.plot(x_train, x_pred, color="red")
plt.title("Matches Played  VS Fifties")
plt.xlabel("Matches Played")
plt.ylabel("Fifties")
plt.show()

data=pd.read_csv("ICC_Test1.csv",encoding= 'unicode_escape')

x=np.array(data['Matches Played']).reshape(-1,1)
y=np.array(data['Centuries'])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)
regressor= LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)
x_pred=regressor.predict(x_train)

plt.scatter(x_train, y_train, color="green")
plt.plot(x_train, x_pred, color="red")
plt.title("Matches Played VS Centuries")
plt.xlabel("Matches Played")
plt.ylabel("Centuries")
plt.show()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
X = [[5, 3], [10, 15], [15, 12], [24, 10], [30, 45], [85, 70]]
y = [0, 1, 1, 0, 1, 0]  # Labels for the samples

# Splitting the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating a KNN classifier object
knn = KNeighborsClassifier(n_neighbors=3)

# Training the classifier
knn.fit(X_train, y_train)

# Predicting labels for the test set
y_pred = knn.predict(X_test)

# Calculating the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
