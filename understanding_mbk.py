from sklearn.cluster import MiniBatchKMeans
import numpy as np
X1 = np.array([[1, 2], [1, 4], [1, 0],
               [4, 2], [4, 0], [4, 4],
               [4, 5], [0, 1], [2, 2],
               [3, 2], [5, 5], [1, -1]])

X2 = np.array([[1, 1], [1.2, 1.2], [1.3, 1.3],
               [1.4, 1.4], [1.5, 1.5], [1.6, 1.6],
               [2, 2], [3, 3], [4, 4],
               [6, 6], [5, 5], [7, 7]])

X = X2

newPoints = [[0, 0], [4, 4]]

# manually fit on batches --------------------------------------------------------------------------
print("PARTIAL FIT", '--> you will only get the labels for the current elements according to the current centroids')
mbk = MiniBatchKMeans(n_clusters=2, random_state = 0, batch_size = 6,)

mbk = mbk.partial_fit(X[0:6, :])
centers0 = mbk.cluster_centers_
print('* centers 0: ', centers0)
labels0 = mbk.labels_
print(' labels0: ', labels0)

mbk = mbk.partial_fit(X[6:12, :])
centers1 = mbk.cluster_centers_ # aca se ve que cambia el centroide mas alto pq llegan valores altos y ese es el que mas se les parece
print('* centers 1: ', centers1, ' --> only the bigger centroid changes with respect to the previous state')
labels1 = mbk.labels_
print(' labels 1: ', labels1)

# predict
p = mbk.predict(newPoints)
print(' prediction for ' + newPoints.__repr__() + ' --> ', p)

print('\n')

# fit on the whole data --------------------------------------------------------------------------
print("FIT THE WHOLE DATASET")
mbk = MiniBatchKMeans(n_clusters=2, random_state = 0, batch_size = 6, max_iter = 10).fit(X)
# TODO: si cambias max_iter a 1 y batch size a 3, cambia el result :)
centers = mbk.cluster_centers_
print('* centers 2: ',centers)
labels = mbk.labels_
print(' labels: ', labels)

# predict same point
p2 = mbk.predict(newPoints)
print(' prediction 2 for ' + newPoints.__repr__() + ' --> ', p2)
