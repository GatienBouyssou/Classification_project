import math
import csv
import numpy as np

data = np.loadtxt("data.txt", delimiter=", ")


def euclideanDistance(currentPoint, line):
    return math.sqrt(pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2))


# euclidean dist without sqrt + size * 0.1
def distance(currentPoint, line):
    return pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2)


def getNextPoint(currentPoint):
    global data
    bestDistance = float('inf')
    bestItem = -1
    for i, line in enumerate(data):
        currentDistance = distance(currentPoint, line)
        if bestDistance > currentDistance:
            bestDistance = currentDistance
            bestItem = i
    result = data[bestItem]
    data = np.delete(data, bestItem, 0)
    return result


if __name__ == '__main__':

    currentPoint = (0,0)
    currentDistanceDone = 0
    totalSize = 0
    resultArray = []

    while currentDistanceDone < 1000:
        nextPoint = getNextPoint(currentPoint)
        currentDistanceDone += euclideanDistance(currentPoint, nextPoint)
        resultArray.append(nextPoint[0])
        currentPoint = (nextPoint[1], nextPoint[2])
        totalSize += nextPoint[3]
        print(currentDistanceDone)
    print(totalSize)
    resultArray.pop()
    print(resultArray)

    # with open('result.csv', 'w+') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=' ',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for cellId in resultArray:
    #         writer.writerow([str(int(cellId))])
