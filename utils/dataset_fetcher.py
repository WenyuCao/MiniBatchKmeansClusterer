import numpy as np
import os
from sys import exit
import csv
from config import getTimeSeriesToyDatasetName, getCsvDatasetsPath

def getTimeSeriesDatasetFromFolder():
    fileFullName = getTimeSeriesToyDatasetName()
    filePath = getCsvDatasetsPath() + fileFullName
    # get the k param from header
    # with open(filePath, newline='') as f:
    #     reader = csv.reader(f)
    #     header = next(reader)  # gets the first line
    # k = header[0] # 'header' returns ['k',]

    # get the data
    ndarray = np.genfromtxt(filePath, delimiter=",", ) # skip_header=1 if header must be skipped
    fileNameWithoutExtension = fileFullName.split(".")[0]
    return ndarray
