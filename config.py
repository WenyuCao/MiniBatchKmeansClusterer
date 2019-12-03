import json

csvDatasetsPath = None
algoNames = None
clusteringResultsPath = None
timeSeriesToyDatasetName = None
timeSeriesDatasetsPath = None

def fetchConfig():
    # we use the global key word to being able to change the values of the variables declared outside the function
    global csvDatasetsPath
    global clusteringResultsPath
    global algoNames
    global timeSeriesToyDatasetName
    global timeSeriesDatasetsPath

    configFilePath = "/home/camila/Desktop/TESIS/DATA/config.json"
    with open(configFilePath) as f:
        data = json.load(f)
    # fill variables
    csvDatasetsPath = data.get("csvDatasetsPath")
    clusteringResultsPath = data.get("clusteringResultsPath")
    algoNames = data.get("algoNames")
    timeSeriesToyDatasetName = data.get("timeSeriesToyDatasetName")
    timeSeriesDatasetsPath = data.get("timeSeriesDatasetsPath")


def getCsvDatasetsPath():
    if csvDatasetsPath is not None:
        return csvDatasetsPath
    # else
    fetchConfig()
    return csvDatasetsPath


def getClusteringResultsPath():
    if clusteringResultsPath is not None:
        return clusteringResultsPath
    # else
    fetchConfig()
    return clusteringResultsPath


def getTimeSeriesToyDatasetName():
    if timeSeriesToyDatasetName is not None:
        return timeSeriesToyDatasetName
    # else
    fetchConfig()
    return timeSeriesToyDatasetName

def getTimeSeriesDatasetsPath():
    if timeSeriesDatasetsPath is not None:
        return timeSeriesDatasetsPath
    # else
    fetchConfig()
    return timeSeriesDatasetsPath


def getMbkName():
    key = "mbk"
    mbkName = algoNames.get(key)
    if (mbkName != None):
        return mbkName
    # else
    fetchConfig()
    return algoNames.get(key)


resourcesFolder = getCsvDatasetsPath()
