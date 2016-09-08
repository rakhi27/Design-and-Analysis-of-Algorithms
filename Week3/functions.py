import random

def randomContractionAlgorithm(edgeList, nodeList):
    # while there are more than 2 vertices
    while len(nodeList) > 2:
        # randomly pick an edge
        edgeIndex = random.randrange(0, len(edgeList))
        nodeU, nodeV = edgeList[edgeIndex]

        # contract vertices u and v and
        nodeList.remove(nodeV)
        newEdgeList = list()
        for i in range(0, len(edgeList)):
            if edgeList[i][0] == nodeV:
                edgeList[i][0] = nodeU
            elif edgeList[i][1] == nodeV:
                edgeList[i][1] = nodeU
            #remove self loops
            if edgeList[i][0] != edgeList[i][1]:
                newEdgeList.append(edgeList[i])
        edgeList =  newEdgeList

    return len(edgeList)