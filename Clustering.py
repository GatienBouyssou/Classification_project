import csv

import numpy as np
import pandas as pd
import math
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.neighbors._kd_tree import KDTree

data_bank = pd.read_csv("data.txt", header=None, delimiter=",")

def euclideanDistance(currentPoint, line):
    return math.sqrt(pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2))

# euclidean dist without sqrt + size * 0.1
def distance(currentPoint, line):
    return (pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2)) * weights[0] + line[3] * weights[1]


def getClosestCluster(distancesPointClusters):
    sortedIndexes = sorted(range(len(distancesPointClusters)), key=lambda k: distancesPointClusters[k])
    clusterForPoint = []
    for clusterIndex in sortedIndexes:
        clusterForPoint = data[data.cluster == clusterIndex]
        if len(clusterForPoint) != 0:
            break
    return clusterForPoint


def getNextPoint(currentPoint, kmeans):
    global data
    bestDistance = float('inf')
    bestItemId = -1
    clusterForPoint = getClosestCluster(kmeans.transform([currentPoint])[0])
    for index, line in clusterForPoint.iterrows():
        currentDistance = distance(currentPoint, line)
        if bestDistance > currentDistance:
            bestDistance = currentDistance
            bestItemId = line[0]
    result = data[data[0] == bestItemId].values[0]
    data = data[data[0] != bestItemId]
    return result


if __name__ == '__main__':
    print("Starting Clustering ...")
    data_train = data_bank.drop([0,3], axis=1)
    kmeans = KMeans(n_clusters=100, random_state=0).fit(data_train)
    data_bank['cluster'] = kmeans.labels_

    print("Clustering Done.")

    arrayResults = []
    for i in range(0, 1):
        data = data_bank.copy()
        weights = [1, 0]
        print("----------------")
        print("Now working on the epoch " + str(i))
        print("----------------")
        currentPoint = [0, 0]
        currentDistanceDone = 0
        totalSize = 0
        resultArray = []
        while currentDistanceDone < 10000:
            nextPoint = getNextPoint(currentPoint, kmeans)
            currentDistanceDone += euclideanDistance(currentPoint, nextPoint)
            resultArray.append(nextPoint[0])
            currentPoint = (nextPoint[1], nextPoint[2])
            totalSize += nextPoint[3]
            print(currentDistanceDone)
        print(totalSize)
        print(resultArray)
        arrayResults.append([weights, totalSize])
        # resultArray.pop()
    print(arrayResults)
    # with open('result.csv', 'w+') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for cellId in resultArray:
    #         writer.writerow([str(int(cellId))])