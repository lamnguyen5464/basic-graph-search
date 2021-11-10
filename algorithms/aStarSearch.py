import heapq
from utilities import getHeuristic, middleware


@middleware
def aStarSearch(n, initNode, endNode, adjacencyList):
    heuristicDistance = {initNode: getHeuristic(n, initNode, endNode) + 0}
    listExpanded = []
    preNodeMap = {}
    queue = []
    # priority queue
    heapq.heappush(queue, (heuristicDistance[initNode], 0, initNode, initNode))

    while (len(queue) != 0):
        (currentHeuristic, currentLength, preNode,
         currentNode) = heapq.heappop(queue)

        if currentNode in heuristicDistance and currentHeuristic > heuristicDistance[currentNode]:
            continue

        listExpanded.append(currentNode)

        preNodeMap[currentNode] = preNode		# for get returnPath

        if currentNode == endNode:
            break

        for nextNode in adjacencyList[currentNode]:
            nextLength = + currentLength + 1
            nextHeuristic = getHeuristic(n, nextNode, endNode) + nextLength

            if not nextNode in heuristicDistance or heuristicDistance[nextNode] > nextHeuristic:
                heuristicDistance[nextNode] = nextHeuristic
                heapq.heappush(
                    queue, (nextHeuristic, nextLength, currentNode, nextNode))

    # get return path
    returnPath = []
    while endNode in preNodeMap and endNode != preNodeMap[endNode]:
        returnPath.append(endNode)
        endNode = preNodeMap[endNode]
    returnPath.append(initNode)
    returnPath.reverse()

    return (listExpanded, returnPath)
