############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 4
# Kosaraju algorithm  - Recursive implementation
# Warning : Doesn't work on big file, due to recursion and memory limits.
# August 2016
############

from collections import defaultdict, Counter
import time, sys



sccList = defaultdict(list)
sccCounter = Counter()
finishingTime = dict()
t = 0
source = None


def dFS_Loop(graph, computationOrder):
    global source, t
    source = None
    t = 0

    #Loop from n to 1
    for nodeHeadKey in reversed(sorted(computationOrder.keys())):
        #Get the node associated with the computationOrder Key
        nodeHead = computationOrder.get(nodeHeadKey)
        if (graph[nodeHead]['exploredVertice'] == False):
            source = nodeHead
            dFS(graph, nodeHead)

    return finishingTime, sccList


def dFS(graph, nodeHead):
    global t, source
    #Mark node as explored
    graph[nodeHead]['exploredVertice'] = True
    #Update Scc list
    sccList[source].append(nodeHead)
    sccCounter[source] += 1

    nodeTailList = graph.get(nodeHead)
    if nodeTailList:
        for nodeTail in nodeTailList['graph']:
            if (graph[nodeTail]['exploredVertice'] == False):
                dFS(graph, nodeTail)
    t += 1
    finishingTime[t] = nodeHead


## Read the file
file = open("test1.txt", "r")
directedGraph = defaultdict(lambda : {'graph': list(), 'exploredVertices': bool()})
reversedGraph = defaultdict(lambda : {'graph': list(), 'exploredVertice': bool()})
computationOrder = dict()
sys.setrecursionlimit(10000000)
startTime = time.clock()
for lines in file:
    col = lines.strip().split()
    #Create a directed graph, in the form {node1 : [node2, node3], explored ? : True/False}
    directedGraph[int(col[0])]['graph'].append(int(col[1]))
    directedGraph[int(col[0])]['exploredVertice'] = False

    #Create a reversed graph, in the form {node1 : [node2, node3], explored ? : True/False}
    reversedGraph[int(col[1])]['graph'].append(int(col[0]))
    reversedGraph[int(col[1])]['exploredVertice'] = False

    #Create the computation order. Initialized at {1:1, 2:2, 3:3 ...}
    computationOrder[int(col[0])] = int(col[0])

print("Read File time: ", time.clock() - startTime, "s")

##Kosaraju's 2 pass algorithm
startTime = time.clock()

#First pass on reversed graph
finishingTime, sccList = dFS_Loop(reversedGraph, computationOrder)

#Finishing time is saved and input as the computation order for the second pass
computationOrder = finishingTime
print(finishingTime)
#Re-initialize the list and the size-counter of the scc, and the finishingTime
sccList = defaultdict(list)
sccCounter = Counter()
finishingTime = dict()

#Second pass on directed graph
finishingTime, sccList = dFS_Loop(directedGraph, computationOrder)
print("Computation time: ", time.clock() - startTime, "s")

#Stroncly connected components and their leaders
print(sccList)
