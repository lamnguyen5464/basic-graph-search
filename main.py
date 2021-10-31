import heapq
from input import HEURISTIC, EDGES
from utilities import getNextNodesAbcOrder

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



def ucs(initNode, endNode):
	distance = { initNode:0 }
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
				heapq.heappush(queue, (currentLength + edgeLength, currentNode, nextNode))


	# get return path
	returnPath = []
	while endNode in preNodeMap and endNode != preNodeMap[endNode]:
		returnPath.append(endNode)
		endNode = preNodeMap[endNode]
	returnPath.append(initNode)
	returnPath.reverse()

	return (listExpanded, returnPath)


startNode = 'A'
endNode = 'S'

print("### LIST EXPANDED ###")
print("dfs: ", dfs(startNode, endNode))
print("bfs: ", bfs(startNode, endNode))
print("ucs: ", ucs(startNode, endNode))