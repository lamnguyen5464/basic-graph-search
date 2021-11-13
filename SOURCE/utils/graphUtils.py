import math

# UTILITIES


def goalTest(listNodes, goalNode):
    for node in listNodes:
        if node == goalNode:
            return True
    return False


def inputGraph(f):
    adjacencyList = []
    n = (int)(f.readline())
    totalLine = n * n
    while totalLine > 0:
        line = [(int)(num) for num in f.readline().split()]
        line.sort()
        adjacencyList.append(line)
        totalLine = totalLine - 1

    endNode = (int)(f.readline())

    return (n, adjacencyList, endNode)


def getCordinate(node, n):
    return ((int)(node / n), node % n)


def getEulerDistance(x, y):
    return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))


def getHeuristic(n, a, b):
    x = getCordinate(a, n)
    y = getCordinate(b, n)
    return getEulerDistance(x, y)
