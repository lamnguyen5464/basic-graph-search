from utilities import getNextNodesAbcOrder

def dfs(_startNode, _endNode):
	def dfsHelper(preNode, currentNode, endNode, listExpanded = [], preNodeMap = {}):
		if currentNode in listExpanded:
			return (listExpanded, preNodeMap)

		preNodeMap[currentNode] = preNode		# for get return path

		if (currentNode == endNode):
			return (listExpanded, preNodeMap) 

		listExpanded.append(currentNode)

		listNextNode = getNextNodesAbcOrder(currentNode)
		for nextNode in listNextNode:
			(listExpanded, preNodeMap) = dfsHelper(currentNode, nextNode, endNode, listExpanded, preNodeMap)

		return (listExpanded, preNodeMap)
	
	# implement call
	(listExpanded, preNodeMap) = dfsHelper(_startNode, _startNode, _endNode)

	# get returnMap
	returnPath = []
	while _endNode in preNodeMap and _endNode != preNodeMap[_endNode]:
		returnPath.append(_endNode)
		_endNode = preNodeMap[_endNode]
	returnPath.append(_startNode)
	returnPath.reverse()

	return (listExpanded, returnPath)