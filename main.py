from sklearn.cluster import MiniBatchKMeans
from utils.dataset_fetcher import getTimeSeriesDatasetFromFolder
from utils.persistor import resetStorage, storeAlgoConfig, storeResult

# reset storage
resetStorage()

# config the algorithm
n_clusters = 2
random_state = 0
batch_size = 6

mbk = MiniBatchKMeans(n_clusters=n_clusters, random_state=random_state, batch_size=batch_size)

# store algo config
algoConfig = {
    "n_clusters": n_clusters,
    "random_state": random_state,
    "batch_size": batch_size
}
storeAlgoConfig(algoConfig)

# get the data
X = getTimeSeriesDatasetFromFolder()

batch = []
tGlobal = 200
ac = 0
time = 0
for d in getTimeSeriesDatasetFromFolder():
    batch.append(d)
    # increment amount of processed elements
    ac += 1
    if ac == tGlobal:
        # "PARTIAL FIT" will only get the labels for the current elements according to the current centroids
        mbk = mbk.partial_fit(batch)
        # get the current centers TODO: store them
        centers = mbk.cluster_centers_
        print(centers , '\n')
        # reset the batch
        batch = []
        # reset the acumulator
        ac = 0
        time = time + tGlobal
        storeResult({"time": time, "result": centers})
