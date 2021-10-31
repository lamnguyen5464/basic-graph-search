import heapq
from input import EDGES
from utilities import getHeuristic

def aStarSearch(initNode, endNode):
	distance = { initNode: getHeuristic(initNode, endNode) + 0 }
	listExpanded = []
	preNodeMap = {}
	queue = []
	heapq.heappush(queue, (distance[initNode], initNode, initNode))		# priority queue

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

			heuristic = getHeuristic(nextNode, endNode) + currentLength + edgeLength

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