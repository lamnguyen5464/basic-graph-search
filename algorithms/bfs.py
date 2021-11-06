from utilities import getNextNodesAbcOrder, output, goalTest


@output
def bfs(initNode, endNode):
    listExpand = []
    preNodeMap = {}
    queue = [(initNode, initNode)]

    while (len(queue) != 0):
        (preNode, currentNode) = queue.pop(0)

        if currentNode in listExpand:
            continue

        preNodeMap[currentNode] = preNode		# for get returnPath
        listExpand.append(currentNode)

        listNextNode = getNextNodesAbcOrder(currentNode)
        # Goal test
        if goalTest(listNextNode, endNode) == True:
            preNodeMap[endNode] = currentNode
            break

        for nextNode in listNextNode:
            queue.append((currentNode, nextNode))

    # get returnMap
    returnPath = []
    while endNode in preNodeMap and endNode != preNodeMap[endNode]:
        returnPath.append(endNode)
        endNode = preNodeMap[endNode]
    returnPath.append(initNode)
    returnPath.reverse()

    return (listExpand, returnPath)
