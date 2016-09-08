############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 3
# Min cut algorithm
# August 2016
############

from Week3.functions import randomContractionAlgorithm
import numpy
import copy
import time



inputArray = list()
edgeList = list()
nodeList = list()
cutsResult = list()

file = open("test1.txt", "r")
for lines in file:
    col = lines.strip().split()
    inputArray.append(col[0:len(col)])

# Convert to int
inputArray = [[int(x) for x in row] for row in inputArray]
nparray = numpy.array(inputArray)

# create 2 adjacency lists
for element in nparray:
    nodeList.append(element[0])
    for edge in element:
        if (element[0] != edge):
            # check if [1,2] and [2,1] are not both present in the list
            if [edge, element[0]] not in edgeList:
                edgeList.append([element[0], edge])

n = len(nodeList)
desiredNumberIter = int(n * numpy.log(n))
desiredNumberIter = int(1000)

print ("Desired number of iteration: ", desiredNumberIter)

starttime = time.clock()

print (edgeList, nodeList)

for i in range(0, desiredNumberIter):
    # Deep copies
    nodeListsCopy = copy.deepcopy(nodeList)
    edgeListCopy = copy.deepcopy(edgeList)

    result = randomContractionAlgorithm(edgeListCopy, nodeListsCopy)
    cutsResult.append(result)

print ("Min Cut: ", min(cutsResult))
print ("Computation time: ", time.clock() - starttime)
