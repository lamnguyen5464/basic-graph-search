from utils.graphUtils import goalTest


def ids(n, _startNode, _endNode, adjacencyList):
    def idsHelper(preNode, currentNode, endNode, listExpanded=[], preNodeMap={}, limit=0):
        if currentNode in listExpanded or limit <= 0:
            return (listExpanded, preNodeMap, False)

        preNodeMap[currentNode] = preNode		# for get return path

        listExpanded.append(currentNode)

        listNextNode = adjacencyList[currentNode]

        # implement goal test
        if goalTest(listNextNode, endNode):
            preNodeMap[endNode] = currentNode
            return (listExpanded, preNodeMap, True)

        for nextNode in listNextNode:
            (listExpanded, preNodeMap, found) = idsHelper(
                currentNode, nextNode, endNode, listExpanded, preNodeMap, limit - 1)

            if found:
                return (listExpanded, preNodeMap, True)

        return (listExpanded, preNodeMap, False)

    # implement call
    limit = 0
    listExpandedOfLimit = {}

    while True:
        (listExpanded, preNodeMap, found) = idsHelper(
            _startNode, _startNode, _endNode, [], {}, limit)

        listExpandedOfLimit["limit - %d" % (limit)] = listExpanded

        if (found):
            break
        limit = limit + 1

    # get returnMap
    returnPath = []
    while _endNode in preNodeMap and _endNode != preNodeMap[_endNode]:
        returnPath.append(_endNode)
        _endNode = preNodeMap[_endNode]
    returnPath.append(_startNode)
    returnPath.reverse()

    return (listExpandedOfLimit, returnPath)
