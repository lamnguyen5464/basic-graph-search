from input import HEURISTIC, EDGES
from functools import wraps
import time

# UTILITIES


def getHeuristic(a, b):
    if not a in HEURISTIC or not b in HEURISTIC:
        return 0

    ha = HEURISTIC[a]
    return ha


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
    def wrapper(startNode, endNode):
        startTime = time.time()
        adjacencyList = input()

        (listExpaned, listReturnPath) = func(
            startNode, endNode, adjacencyList)

        print("- List expanded: ", listExpaned)
        print("- List return path: ", listReturnPath)
        print("- Duration: ", time.time() - startTime, "(ms)")
    return wrapper


def goalTest(listNodes, goalNode):
    for node in listNodes:
        if node == goalNode:
            return True
    return False


def input():
    data = []
    with open('INPUT.txt', 'r') as f:
        n = [(int)(num) for num in f.readline().split()][0]		# get a number
        n = n * n
        while n > 0:
            line = [(int)(num) for num in f.readline().split()]
            n = n - 1
            data.append(line)

    return data


def getCordinate(node, n):
    return ((int)(node / n), node % n)
