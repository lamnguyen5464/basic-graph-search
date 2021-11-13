import heapq
from utils.graphUtils import getHeuristic, goalTest


def gbfs(n, initNode, endNode, adjacencyList):
    distance = {initNode: getHeuristic(n, initNode, endNode)}
    listExpanded = []
    preNodeMap = {}
    queue = []
    # priority queue
    heapq.heappush(queue, (distance[initNode], initNode, initNode))
    signalStop = False

    while (len(queue) != 0 and not signalStop):
        (currentLength, preNode, currentNode) = heapq.heappop(queue)

        if currentNode in distance and currentLength > distance[currentNode]:
            continue

        preNodeMap[currentNode] = preNode		# for get returnPath

        listExpanded.append(currentNode)

        # Goal test
        if goalTest(adjacencyList[currentNode], endNode) == True:
            preNodeMap[endNode] = currentNode
            break

        for nextNode in adjacencyList[currentNode]:
            heuristic = getHeuristic(n, nextNode, endNode)

            if not nextNode in distance or distance[nextNode] > heuristic:
                distance[nextNode] = heuristic
                heapq.heappush(queue, (heuristic, currentNode, nextNode))

    # get return path
    returnPath = []
    while endNode in preNodeMap and endNode != preNodeMap[endNode]:
        returnPath.append(endNode)
        endNode = preNodeMap[endNode]
    returnPath.append(initNode)
    returnPath.reverse()

    return (len(listExpanded) + 1, listExpanded, returnPath)
