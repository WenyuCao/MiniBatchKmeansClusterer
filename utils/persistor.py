import json

import numpy as np
import os
from config import getClusteringResultsPath, getMbkName, getTimeSeriesDatasetsPath, getTimeSeriesToyDatasetName
import shutil

folder = getClusteringResultsPath() + getTimeSeriesToyDatasetName() + '/' + getMbkName() + '/'


def resetStorage():
    if os.path.exists(folder):
        shutil.rmtree(folder)


def createDirectoryIfNotExists(folder):
    # check if resourcesFolder needs to be created
    if not os.path.exists(folder):
        os.makedirs(folder)


def storeResult(snapshot):
    createDirectoryIfNotExists(folder)
    time = snapshot.get("time")
    result = snapshot.get("result")
    targetFile = folder + str(time) + '.csv'
    np.savetxt(targetFile, result, delimiter=',',)


def storeAlgoConfig(dict):
    createDirectoryIfNotExists(folder)
    file = folder + 'algoConfig.json'
    with open(file, 'w') as outfile:
        json.dump(dict, outfile)

