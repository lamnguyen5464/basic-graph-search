import heapq
from input import HEURISTIC, EDGES
from utilities import getNextNodesAbcOrder

def bfs(initNode, endNode):
	listExpand = []
	queue = [initNode]

	while (len(queue) != 0):
		currentNode = queue.pop(0)

		if currentNode in listExpand:
			continue

		listExpand.append(currentNode)
		listNextNode = getNextNodesAbcOrder(currentNode)

		for nextNode in listNextNode:
			if nextNode == endNode:
				return listExpand
			queue.append(nextNode)
	
	return listExpand

def dfs(currentNode, endNode, listExpanded = []):
	if currentNode in listExpanded or currentNode == endNode:
		return listExpanded

	listExpanded.append(currentNode)

	listNextNode = getNextNodesAbcOrder(currentNode)
	for nextNode in listNextNode:
		listExpanded = dfs(nextNode, endNode, listExpanded)

	return listExpanded


def ucs(initNode, endNode):
	listExpanded = []
	distance = {initNode:0}
	queue = []
	heapq.heappush(queue, (0, initNode))		# priority queue

	while (len(queue) != 0):
		(currentLength, currentNode) = heapq.heappop(queue)

		if currentNode in distance and currentLength > distance[currentNode]:
			continue

		listExpanded.append(currentNode)

		if currentNode == endNode:
			break

		for e in EDGES:
			if e[0] != currentNode and e[1] != currentNode:
				continue
			nextNode = e[0] == currentNode and e[1] or e[0]
			edgeLength = e[2]

			if not nextNode in distance or distance[nextNode] > currentLength + edgeLength:
				distance[nextNode] = currentLength + edgeLength
				heapq.heappush(queue, (currentLength + edgeLength, nextNode))
	
	return listExpanded


startNode = 'A'
endNode = 'S'

print("### LIST EXPANDED ###")
print("dfs: ", dfs(startNode, endNode))
print("bfs: ", bfs(startNode, endNode))
print("ucs: ", ucs(startNode, endNode))