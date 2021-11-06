from utilities import getNextNodesAbcOrder, output, goalTest


@output
def dfs(_startNode, _endNode):
    def dfsHelper(preNode, currentNode, endNode, listExpanded=[], preNodeMap={}):
        if currentNode in listExpanded:
            return (listExpanded, preNodeMap, False)

        preNodeMap[currentNode] = preNode		# for get return path

        if (currentNode == endNode):
            return (listExpanded, preNodeMap, True)

        listExpanded.append(currentNode)

        listNextNode = getNextNodesAbcOrder(currentNode)

        # implement goal test
        if goalTest(listNextNode, endNode):
            preNodeMap[endNode] = currentNode
            return (listExpanded, preNodeMap, True)

        for nextNode in listNextNode:
            (listExpanded, preNodeMap, found) = dfsHelper(
                currentNode, nextNode, endNode, listExpanded, preNodeMap)

            if found:
                return (listExpanded, preNodeMap, True)

        return (listExpanded, preNodeMap, False)

    # implement call
    (listExpanded, preNodeMap, _) = dfsHelper(
        _startNode, _startNode, _endNode)

    # get returnMap
    returnPath = []
    while _endNode in preNodeMap and _endNode != preNodeMap[_endNode]:
        returnPath.append(_endNode)
        _endNode = preNodeMap[_endNode]
    returnPath.append(_startNode)
    returnPath.reverse()

    return (listExpanded, returnPath)
