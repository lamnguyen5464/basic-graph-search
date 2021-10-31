from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.ucs import ucs
from algorithms.gbfs import gbfs
from algorithms.aStarSearch import aStarSearch


startNode = 'A'
endNode = 'S'

print("### ( [LIST EXPANDED], [LIST RETURN PATH] ) ###")

print("dfs: ", dfs(startNode, endNode))
print("bfs: ", bfs(startNode, endNode))
print("ucs: ", ucs(startNode, endNode))
print("gbfs: ", gbfs(startNode, endNode))
print("aStarSearch: ", aStarSearch(startNode, endNode))