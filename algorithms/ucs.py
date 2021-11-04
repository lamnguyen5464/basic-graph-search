import heapq
from input import EDGES
from utilities import output


@output
def ucs(initNode, endNode):
    distance = {initNode: 0}
    listExpanded = []
    preNodeMap = {}
    queue = []
    heapq.heappush(queue, (0, initNode, initNode))		# priority queue

    while (len(queue) != 0):
        (currentLength, preNode, currentNode) = heapq.heappop(queue)

        if currentNode in distance and currentLength > distance[currentNode]:
            continue

        listExpanded.append(currentNode)

        preNodeMap[currentNode] = preNode		# for get returnPath

        if currentNode == endNode:
            break

        for e in EDGES:
            if e[0] != currentNode and e[1] != currentNode:
                continue

            edgeLength = e[2]
            nextNode = e[0] == currentNode and e[1] or e[0]

            if not nextNode in distance or distance[nextNode] > currentLength + edgeLength:
                distance[nextNode] = currentLength + edgeLength
                heapq.heappush(
                    queue, (currentLength + edgeLength, currentNode, nextNode))

    # get return path
    returnPath = []
    while endNode in preNodeMap and endNode != preNodeMap[endNode]:
        returnPath.append(endNode)
        endNode = preNodeMap[endNode]
    returnPath.append(initNode)
    returnPath.reverse()

    return (listExpanded, returnPath)
