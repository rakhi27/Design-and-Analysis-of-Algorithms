############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 4
# Kosaraju algorithm  - Iterative implementation
# August 2016
############

from collections import defaultdict, Counter, deque
import time

sccList = defaultdict(list)
sccCounter = Counter()
finishingTime = dict()
t = 0
source = None
exploredVertice = dict()


def dFS_Loop(graph, computationOrder):
    global source, t
    source = None
    t = 0

    # Loop from n to 1
    for nodeHeadKey in reversed(sorted(computationOrder.keys())):
        # Get the node associated with the computationOrder Key
        nodeHead = computationOrder.get(nodeHeadKey)
        source = nodeHead
        if (exploredVertice.get(nodeHead, False) == False):
            dFS(graph, nodeHead)

    return finishingTime, sccList


def dFS(graph, nodeHead):
    global t, source
    stack = deque()

    # Mark node as explored
    exploredVertice[nodeHead] = True

    # Stack (LIFO) initialized with nodeHead
    stack.appendleft(nodeHead)

    while stack:
        flag = 0

        # Remove first node of the stack
        nodeHead = stack[0]

        # Get all the nodes accessible from this node
        nodeTailList = graph.get(nodeHead)
        if nodeTailList:  # Check if the list is not empty before iterate
            for nodeTail in nodeTailList:
                if (exploredVertice.get(nodeTail, False) == False):
                    # Mark node as explored
                    exploredVertice[nodeTail] = True

                    # Add nodeTail to top of the stack
                    stack.appendleft(nodeTail)

                    flag = 1
                    break

        if (flag == 0):
            # Store finishing time
            t += 1
            finishingTime[t] = nodeHead

            # Store the Scc and count
            sccList[source].append(nodeHead)
            sccCounter[source] += 1

            # Remove from stack
            stack.popleft()


## Read the file
directedGraph = defaultdict(list)
reversedGraph = defaultdict(list)
computationOrder = dict()


file = open("scc.txt", "r")
startTime = time.clock()
for lines in file:
    col = lines.strip().split()
    nodeHead = int(col[0])
    nodeTail = int(col[1])

    # Create a directed graph, in the form {node1 : [node2, node3], explored ? : True/False}
    directedGraph[nodeHead].append(nodeTail)

    # Create a reversed graph, in the form {node1 : [node2, node3], explored ? : True/False}
    reversedGraph[nodeTail].append(nodeHead)

    # Create computation order
    computationOrder[nodeTail]=nodeTail
    computationOrder[nodeHead]=nodeHead

print("Read File time: %.5f" % ( time.clock() - startTime), "s")

##Kosaraju's 2 pass algorithm
startTime = time.clock()

# First pass on reversed graph
finishingTime, sccList = dFS_Loop(reversedGraph, computationOrder)

# Finishing time is saved and input as the computation order for the second pass
computationOrder = finishingTime

# Re-initialize the list and the size-counter of the scc, and the finishingTime
sccList = defaultdict(list)
sccCounter = Counter()
finishingTime = dict()
exploredVertice = dict()

# Second pass on directed graph
finishingTime, sccList = dFS_Loop(directedGraph, computationOrder)
print("Computation time: %.5f" % (time.clock() - startTime), "s")

# Print the size of the 5 biggest scc
fiveBiggest = sccCounter.most_common(5)
print(fiveBiggest)
