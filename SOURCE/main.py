from algorithms.ucs import ucs
from algorithms.ids import ids
from algorithms.gbfs import gbfs
from algorithms.aStarSearch import aStarSearch
from utils.graphUtils import inputGraph
from utils.osUtils import getFilesInDir, getRootDir
import time
import json


inputDir = getRootDir() + "/INPUT/"
outputDir = getRootDir() + "/OUTPUT/"

listInputFiles = getFilesInDir(inputDir)

methods = [
    ucs,
    ids,
    aStarSearch,
    gbfs
]

for testFile in listInputFiles:

    output = {}

    # input
    file = open(inputDir + testFile, 'r')
    (n, adjacencyList, endNode) = inputGraph(file)
    file.close()

    # implement
    for method in methods:
        startTime = time.time()
        (listExpanded, listReturnPath) = method(n, 0, endNode, adjacencyList)

        res = {}
        res["duration"] = str(time.time() - startTime) + "(s)"
        res["listExpaned"] = listExpanded
        res["listReturnPath"] = listReturnPath

        output[method.__name__] = res

    # output
    file = open(outputDir + testFile, 'w')
    file.write(json.dumps(output, sort_keys=False, indent=4))
