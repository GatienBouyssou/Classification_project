import matplotlib.pyplot as plt
import matplotlib as mp
import pandas as pd

data = pd.read_csv("data.txt", header=None, delimiter=",")
data.columns = ['id', 'x', 'y', 'sizePoint']

def getFrequencySize():
    abscissa = []
    arrayResult = []
    lenData = len(data)
    for i in range(10, 110, 10):
        abscissa.append(i)
        arrayResult.append(len(data[(data.sizePoint > i - 10) & (data.sizePoint < i)]) / lenData)
    plt.bar(abscissa, arrayResult)
    plt.title("The proportion of sizes per range of 10")
    plt.ylabel("Frequency")
    plt.xlabel("Upper bounds of the ranges")
    plt.savefig("../projectFiguresAndData/freqSizePerRange10")
    plt.show()

def plotPointsWithSizeAsColor():
    abscissa = []
    ordinate = []
    meanSizePerRegions = []
    step = 10
    for x in range(-90, 100, step):
        for y in range(-90, 100, step):
            abscissa.append(x)
            ordinate.append(y)
            conditionX = ((data.x > x - step) & (data.x < x + step))
            conditionY = ((data.y > y - step) & (data.y < y + step))
            pointInArea = data[conditionX & conditionY]
            if len(pointInArea) == 0:
                meanForArea = 0
            else:
                meanForArea = sum(pointInArea.sizePoint)/len(pointInArea)
            meanSizePerRegions.append(meanForArea)
    print(meanSizePerRegions)
    plt.scatter(abscissa, ordinate, c=meanSizePerRegions, cmap=plt.cm.winter)
    plt.xlabel("X coordinates")
    plt.ylabel("Y coordinates")
    plt.title("Mean size per regions")
    plt.colorbar()
    plt.savefig("../projectFiguresAndData/MeanSizePerRegions")
    plt.show()

if __name__ == '__main__':
    plotPointsWithSizeAsColor()
