############
# Pecoraro Cyril
# Design and Analysis of Algorithms - Week 5
# Dijkstra Shortest path algorithm
# Implementation as described in the lectures
# August 2016
############

from collections import defaultdict, deque
import time

exploredNodes = dict()
distanceNode = dict()


def dijkstra(graph):
    # Source vertex is the first vertex of the graph
    sourceVertex = next(graph.__iter__())
    # Set it as new vertex V
    vertexV = sourceVertex

    # Set distance for source vertex:
    distanceNode[sourceVertex] = 0

    # Mark source as explored
    exploredNodes[sourceVertex] = True

    while len(exploredNodes) != len(graph):

        # Among the neighbours of this node V, pick a node that has not been explored
        vertexV_neighbours = graph[vertexV]
        for vertexW, distanceW in vertexV_neighbours:
            if exploredNodes.get(vertexW, False) == False:

                # Calculate the distance
                l_vw = distanceNode[vertexV] + distanceW

                # Dijkstra criteria
                if vertexW in distanceNode.keys():
                    if distanceNode[vertexW] > l_vw:
                        distanceNode[vertexW] = l_vw
                else:
                    distanceNode[vertexW] = l_vw

        # Pick the vertex with minimum distance value and not already visited
        distanceNodeCalculation = dict()
        for k, v in distanceNode.items():
            if exploredNodes.get(k, False) == False:
                distanceNodeCalculation[k] = v
        vertexW_star = min(distanceNodeCalculation, key=distanceNodeCalculation.get)

        # Mark node as explored
        exploredNodes[vertexW_star] = True

        # Set it as new vertex V
        vertexV = vertexW_star

    return distanceNode


## Read the file
inputGraph = defaultdict(list)

file = open("dijkstra.txt", "r")
startTime = time.clock()
for lines in file:
    col = lines.strip().split()

    # Create a directed graph, in the form {node1 : [nodeY1, weightY1],[nodeY2, weightY2] }
    node = int(col[0])

    for c in range(1, len(col)):
        nodeY_weightY = col[c].split(',')
        inputGraph[node].append([int(nodeY_weightY[0]), int(nodeY_weightY[1])])

print("Read File time: %.5f" % (time.clock() - startTime), "s")

startTime = time.clock()
distanceNode = dijkstra(inputGraph)
print("Computation time: %.5f" % (time.clock() - startTime), "s")

# In the assignment, it is asked to find distance to nodes:7,37,59,82,99,115,133,165,188,197
assignementNodesRequest = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
print("Assignment answer:")
for n in assignementNodesRequest:
    print(distanceNode[n], end=",")
