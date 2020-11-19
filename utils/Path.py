from Classification_project.utils.Point import Point


class Path:
    def basicInit(self, currentPoint=Point(), distance=0.0, score=0.0):
        self.currentPoint = currentPoint
        self.path = []
        self.distance = distance
        self.score = score
        return self

    def initFromPath(self, path):
        return self.basicInit(path.currentPoint, path.distance, path.score)

    def moveToPoint(self, line):
        self.distance += self.currentPoint.euclideanDistance(line)
        self.currentPoint = Point(line.x, line.y)
        self.path.append(line.id)
        self.score += line.sizePoint

    def mergePaths(self, path):
        self.distance = path.distance
        self.score = path.score
        self.currentPoint = path.currentPoint
        self.path.extend(path.path)

    def isPointInPath(self, lineId):
        return lineId in self.path

    def toString(self):
        return "Distance done : " + str(self.distance) + " sizePoint done : " + str(self.score)

    def removeLastPoint(self, data):
        line = data.loc[self.path[len(self.path) - 2]]
        curLine = data.loc[self.path[len(self.path) - 1]]
        self.distance -= self.currentPoint.euclideanDistance(line)
        self.currentPoint = Point(line.x, line.y)
        self.path.pop()
        self.score -= curLine.sizePoint