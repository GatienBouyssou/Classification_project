import math
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def euclideanDistance(currentPoint, line):
    return math.sqrt(pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2))


# euclidean dist without sqrt + size * 0.1
def distance(currentPoint, line):
    return pow(currentPoint[0] - line[1], 2) + pow(currentPoint[1] - line[2], 2)

def getData(currentPoint, diameter):
    conditionX = ((data.x > currentPoint[0] - diameter) & (data.x < currentPoint[0] + diameter))
    conditionY = ((data.y > currentPoint[1] - diameter) & (data.y < currentPoint[1] + diameter))
    return data[conditionX & conditionY]

def getNextPoint(currentPoint):
    global data
    bestDistance = float('inf')
    bestItem = -1
    neighbourPoints = []
    diameter = 5
    while len(neighbourPoints) == 0:
        neighbourPoints = getData(currentPoint, diameter)
        diameter += 5

    for i, line in neighbourPoints.iterrows():
        currentDistance = distance(currentPoint, line)
        if bestDistance > currentDistance:
            bestDistance = currentDistance
            bestItem = line.id
    result = data.loc[bestItem]
    data = data.drop(bestItem)
    return result


if __name__ == '__main__':
    # abscissa = []
    # results = []
    # for i in range(20,30,1):
    data = pd.read_csv("data.txt", header=None, delimiter=",")
    data.columns = ['id', 'x', 'y', 'sizePoint']
    # abscissa.append(i)
    # print("----------------")
    # print("Now working with the weight " + str(i))
    # print("----------------")
    currentPoint = (0,0)
    currentDistanceDone = 0
    totalSize = 0
    resultArray = []
    data = data[data.sizePoint > 0]
    print(len(data))
    while currentDistanceDone < 10000:
        nextPoint = getNextPoint(currentPoint)
        currentDistanceDone += euclideanDistance(currentPoint, nextPoint)
        resultArray.append(nextPoint[0])
        currentPoint = (nextPoint[1], nextPoint[2])
        totalSize += nextPoint[3]
        # print(currentDistanceDone)
    print(totalSize)
    resultArray.pop()
    print(resultArray)
        # results.append(totalSize)
    # with open('result.csv', 'w+') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=' ',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for cellId in resultArray:
    #         writer.writerow([str(int(cellId))])
    # plt.plot(abscissa, results)
    # plt.title("Results of the algorithm when removing smallest Cells")
    # plt.ylabel("Result")
    # plt.xlabel("Remove cells under")
    # plt.savefig("../projectFiguresAndData/resultDeleteData")
    # plt.show()
