import heapq


def ucs(n, initNode, endNode, adjacencyList):
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

        for nextNode in adjacencyList[currentNode]:
            if not nextNode in distance or distance[nextNode] > currentLength + 1:
                distance[nextNode] = currentLength + 1
                heapq.heappush(
                    queue, (currentLength + 1, currentNode, nextNode))

    # get return path
    returnPath = []
    while endNode in preNodeMap and endNode != preNodeMap[endNode]:
        returnPath.append(endNode)
        endNode = preNodeMap[endNode]
    returnPath.append(initNode)
    returnPath.reverse()

    return (listExpanded, returnPath)
