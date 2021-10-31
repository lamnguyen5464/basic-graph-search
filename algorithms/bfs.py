from utilities import getNextNodesAbcOrder, output

@output
def bfs(initNode, endNode):
	listExpand = []
	preNodeMap = {}
	queue = [(initNode, initNode)]
	signalStop = False

	while (len(queue) != 0 and not signalStop):
		(preNode, currentNode) = queue.pop(0)

		if currentNode in listExpand:
			continue

		preNodeMap[currentNode] = preNode		# for get returnPath
		listExpand.append(currentNode)

		listNextNode = getNextNodesAbcOrder(currentNode)
		for nextNode in listNextNode:

			if nextNode == endNode:	# stop here
				signalStop = True
				preNodeMap[nextNode] = currentNode

			queue.append((currentNode, nextNode))
	

	# get returnMap
	returnPath = []
	while endNode in preNodeMap and endNode != preNodeMap[endNode]:
		returnPath.append(endNode)
		endNode = preNodeMap[endNode]
	returnPath.append(initNode)
	returnPath.reverse()

	return (listExpand, returnPath)