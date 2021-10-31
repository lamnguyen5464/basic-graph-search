from input import HEURISTIC, EDGES

# UTILITIES
def getHeuristic(a, b):
	if not a in HEURISTIC or not b in HEURISTIC:
		return 0;

	ha = HEURISTIC[a]
	hb = HEURISTIC[b]

	return abs(ha[0] - hb[0]) + abs(ha[1] - hb[1])

def initVisitedList():
	visited = {}
	for e in EDGES:
		visited[e[0]] = False
		visited[e[1]] = False
	return visited

def getNextNodesAbcOrder(currentNode):
	list = []
	for e in EDGES:
		if e[0] != currentNode and e[1] != currentNode:
			continue
		nextNode = e[0] == currentNode and e[1] or e[0]
		list.append(nextNode)

	list.sort()
	return list

######################################################################