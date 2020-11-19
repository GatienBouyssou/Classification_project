import copy
import csv

import matplotlib.pyplot as plt

from Classification_project.utils.Path import Path
import pandas as pd

def getData(data, currentPoint, diameter):
    conditionX = ((data.x > currentPoint.x - diameter) & (data.x < currentPoint.x + diameter))
    conditionY = ((data.y > currentPoint.y - diameter) & (data.y < currentPoint.y + diameter))
    return data[conditionX & conditionY]

def getNextPoint(dataRemaining, width, depth, currentPath, currentDepth=0, weight=0):
    bestDistances = [[float('inf'), -1] for i in range(0, width)]
    currentPoint = currentPath.currentPoint

    neighbourPoints = pd.DataFrame()
    diameter = 5
    while len(neighbourPoints) < width:
        neighbourPoints = getData(dataRemaining, currentPoint, diameter)
        diameter += 5

    for line in neighbourPoints.itertuples():
        currentDistance = currentPoint.distance(line)
        for bestElementIndex in range(0, width):
            bestElement = bestDistances[bestElementIndex]
            if bestElement[0] > currentDistance:
                bestDistances.insert(bestElementIndex, [currentDistance, line])
                bestDistances.pop()
                break

    if depth == currentDepth:
        if not type(bestDistances[0][1]) == int:
            currentPath.moveToPoint(bestDistances[0][1])
        return currentPath
    else:
        bestPath = Path().basicInit(distance=float("inf"))
        for bestChoice in bestDistances:
            if type(bestChoice[1]) == int: break
            newPath = copy.deepcopy(currentPath)
            newPath.moveToPoint(bestChoice[1])
            newData = dataRemaining.drop(bestChoice[1].id)
            current = getNextPoint(newData, width, depth, newPath, currentDepth=currentDepth + 1, weight=weight)
            difDistance = current.distance - bestPath.distance
            # difScore = (current.score - bestPath.score)/weight
            # if difDistance < 0 and difScore < abs(difDistance) or difDistance > 0 and difScore > abs(difDistance):
            if difDistance < 0:
                bestPath = current
        return bestPath

if __name__ == '__main__':
    widthToUse = 3
    depthToUse = 4
    # abscissa = []
    # results = []
    # for i in range(500,2000,500):
    #     abscissa.append(i)
    #     weight = i
    #     print("----------------")
    #     print("Now working with the weight " + str(weight))
    #     print("----------------")
    data = pd.read_csv("data.txt", header=None, delimiter=",")
    data.columns = ['id', 'x', 'y', 'sizePoint']
    data = data[data.sizePoint > 27]
    print(len(data))
    data_save = data.copy()
    resultPath = Path().basicInit()
    while resultPath.distance <= 10000:
        nextPoints = getNextPoint(data, widthToUse, depthToUse, Path().initFromPath(resultPath), weight=500)
        # resultPath.moveToPoint(data.loc[nextPoints.path[0]])
        # data = data.drop(nextPoints.path[0])
        resultPath.mergePaths(nextPoints)
        data = data[~data.id.isin(nextPoints.path)]
        print(resultPath.distance)
    print(resultPath.score)
    while resultPath.distance > 10000:
        resultPath.removeLastPoint(data_save)
    print(resultPath.score)
    print(resultPath.path)
        # results.append(resultPath.score)
    # with open('result.csv', 'w+') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=' ',
    #                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     for cellId in resultPath.path:
    #         writer.writerow([str(int(cellId))])
    # plt.bar(abscissa, results, width=300)
    # plt.title("Results of the algorithm for each Beta")
    # plt.ylabel("Result")
    # plt.xlabel("Beta")
    # plt.savefig("../projectFiguresAndData/resultForBeta500")
    # plt.show()
