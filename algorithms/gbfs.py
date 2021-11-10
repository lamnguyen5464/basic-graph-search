import heapq
from input import EDGES
from utilities import getHeuristic, middleware


@middleware
def gbfs(initNode, endNode):
    distance = {initNode: getHeuristic(initNode, endNode)}
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

        for e in EDGES:
            if e[0] != currentNode and e[1] != currentNode:
                continue

            nextNode = e[0] == currentNode and e[1] or e[0]

            if (nextNode == endNode):
                preNodeMap[nextNode] = currentNode		# for get returnPath
                signalStop = True
                break

            heuristic = getHeuristic(nextNode, endNode)

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

    return (listExpanded, returnPath)
