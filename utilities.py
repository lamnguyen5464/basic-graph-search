from input import HEURISTIC, EDGES
from functools import wraps

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


def output(func):
    @wraps(func)
    def wrapper(startNode, endNode):
        (listExpaned, listReturnPath) = func(startNode, endNode)
        print("- List expanded: ", listExpaned)
        print("- List return path: ", listReturnPath)
    return wrapper
