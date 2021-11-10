from input import HEURISTIC, EDGES
from functools import wraps
import time
import math

# UTILITIES


def getHeuristic(n, a, b):
    x = getCordinate(a, n)
    y = getCordinate(b, n)
    return getEulerDistance(x, y)


def initVisitedList():
    visited = {}
    for e in EDGES:
        visited[e[0]] = False
        visited[e[1]] = False
    return visited


def getNextNodesAbcOrder(currentNode):
    list = []
    for e in EDGES:
        if e[0] != currentNode and e[1] != currentNode:
            continue
        nextNode = e[0] == currentNode and e[1] or e[0]
        list.append(nextNode)

    list.sort()
    return list


def middleware(func):
    @wraps(func)
    def wrapper():
        print(func.__name__)
        startTime = time.time()
        (n, adjacencyList, endNode) = input()

        (listExpaned, listReturnPath) = func(
            n, 0, endNode, adjacencyList)

        print("- List expanded: ", listExpaned)
        print("- List return path: ", listReturnPath)
        print("- Duration: ", (time.time() - startTime), "(s)")
        print()
    return wrapper


def goalTest(listNodes, goalNode):
    for node in listNodes:
        if node == goalNode:
            return True
    return False


def input():
    adjacencyList = []
    with open('INPUT.txt', 'r') as f:
        n = [(int)(num) for num in f.readline().split()][0]		# get a number
        totalLine = n * n
        while totalLine > 0:
            line = [(int)(num) for num in f.readline().split()]
            totalLine = totalLine - 1
            adjacencyList.append(line)

        endNode = [(int)(num)
                   for num in f.readline().split()][0]		# get a number

    return (n, adjacencyList, endNode)


def getCordinate(node, n):
    return ((int)(node / n), node % n)


def getEulerDistance(x, y):
    return math.sqrt(math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2))
