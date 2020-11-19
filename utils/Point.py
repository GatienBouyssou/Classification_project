import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def euclideanDistance(self, line):
        return math.sqrt(pow(self.x - line.x, 2) + pow(self.y - line.y, 2))

    # euclidean dist without sqrt + sizePoint * 0.1
    def distance(self, line):
        return (pow(self.x - line.x, 2) + pow(self.y - line.y, 2)) #+ line.sizePoint

    def toArray(self):
        return [self.x, self.y]

    def __eq__(self, other):
        if type(self) == type(other):
            if self.x == other.x and self.y == other.y:
                return True
        return False