from functools import wraps
import time
import math

# UTILITIES


def middleware(func):
    @wraps(func)
    def wrapper():
        startTime = time.time()
        (n, adjacencyList, endNode) = input()

        (listExpaned, listReturnPath) = func(
            n, 0, endNode, adjacencyList)

        with open('OUTPUT', 'a') as f:
            f.write(func.__name__ + "\n")
            f.write("- List expanded: " + str(listExpaned) + "\n")
            f.write("- List return path: " + str(listReturnPath) + "\n")
            f.write("- Duration: " + str(time.time() - startTime) + "(s)" + "\n")
            f.write("\n")
    return wrapper


def goalTest(listNodes, goalNode):
    for node in listNodes:
        if node == goalNode:
            return True
    return False


def input():
    adjacencyList = []
    with open('INPUT', 'r') as f:
        n = (int)(f.readline())
        totalLine = n * n
        while totalLine > 0:
            line = [(int)(num) for num in f.readline().split()]
            totalLine = totalLine - 1
            adjacencyList.append(line)

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


def clearOutput():
    with open('OUTPUT', 'w') as f:
        f.write("")
