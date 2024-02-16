# importing "heapq" to implement heap queue
import heapq
import math
INFINITY = math.inf


Graph = {
    "A": [("B", 20), ("D", 21), ("E", 22)],
    "B": [("A", 20), ("C", 15), ("D", 43), ("H", 80)],
    "C": [("B", 15), ("G", 28)],
    "D": [("A", 21), ("B", 43)],
    "E": [("A", 22)],
    "F": [("D", 26), ("H", 27)],
    "G": [("C", 28), ("H", 64)],
    "H": [("B", 80), ("F", 27), ("G", 64)],
}


# initializing list
li = [("f", 5), ("d", 7), ("s", 9), ("r", 1), ("y", 3)]

# using heapify to convert list into heap
heapq.heapify(li)


# printing created heap
# print("The created heap is : ", (li))
heapq.heapreplace(li, ("f", 6))

# print("The created heap is : ", (li))


def read_problems(problems, input_file):
    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    i = 0
    temporaryTable = []
    listOfProblems = []
    for line in lines:
        i += 1
        if (i == 1):
            continue

        if (len(line.split(" ")) == 1):
            start = i+1
            finish = i + int(line)

        if (i >= start and i <= finish):
            (a, b) = line.strip().split(" ")
            temporaryTable.append((float(a), float(b)))

        if (i == finish):
            listOfProblems.append(temporaryTable)
            temporaryTable = []
    file.close()
    return listOfProblems


def pointInTheZoneOfAnotherPoint(x, y, xs, ys, aroundValue):
    # Verify if the point(xs,ys) is around the point(x,y)
    cond1 = (x-aroundValue <= xs and xs <= x+aroundValue)
    cond2 = (y-aroundValue <= ys and ys <= y+aroundValue)
    return cond1 and cond2


def allPointAround(indexOfThePoint, problem, aroundValue):
    # Problem is a list of coordinates
    allPoints = []
    if (indexOfThePoint >= len(problem)):
        return []
    else:
        x, y = problem[indexOfThePoint]
        for i in range(0, len(problem)):
            xs, ys = problem[i]
            if (pointInTheZoneOfAnotherPoint(x, y, xs, ys, aroundValue)):
                if (x != xs or y != ys):
                    allPoints.append(i)

    if (len(allPoints) == 0):
        return (allPointAround(indexOfThePoint, problem, aroundValue**2))
    return allPoints


def distanceBetweenToPoint(index1, index2, problem):
    if (max(index1, index2) >= len(problem)):
        return 0
    x1, y1 = problem[index1]
    x2, y2 = problem[index2]
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

# print(listofProblems[0])
# print(listofProblems[0][0])


def initialisationOfEdges(problem):
    edges = {}
    aroundValue = (len(problem))**10
    for i in range(0, (len(problem))):
        ptAround = allPointAround(i, problem, aroundValue)
        for j in ptAround:
            # i and j are number
            key = (i, j)
            if (j, i) in edges:
                continue
            else:
                edges[key] = (distanceBetweenToPoint(i, j, problem))
    return edges


def initialisationOfNodes(problem):
    nodes = {}
    nodes["0"] = 0
    for i in range(1, len(problem)):
        nodes[str(i)] = INFINITY
    return nodes


""" 
create a function that verify if the graphe is connexe !!!!
"""


def createListOfNode(dictOfNodes):
    nodeList = []
    for key in dictOfNodes:
        nodeKey = key
        weigth = nodesGraph[key]
        nodeList.append((weigth, nodeKey))
    return nodeList


def getNodeA(a, list):
    # return index of the couple (cost, a) in the list of node
    for tuple in list:
        cost, nodeName = tuple
        if (int(nodeName) == int(a)):
            return tuple
    return


def editCostofNodeA(a, newCost, list):
    # return the same list with a new cost the couple (cost, a) in the list of node
    tupleToEdit = getNodeA(a, list)
    list.remove(tupleToEdit)
    tupleToEdit = (newCost, str(a))
    list.append(tupleToEdit)
    return list


def getMinNode(list):
    # return the element with the smallest cost in couple (cost, a) in the list of node
    return min(list)


def removeMinNode(list):
    # return the list without the smallest cost in couple (cost, a) in the list of node
    list.remove(min(list))
    return list


def removeNodeA(a, list):
    # return the list without the smallest cost in couple (cost, a) in the list of node
    list.remove(getNodeA(a, list))
    return list


def shortestEdge(edgeList, dictOfEdge):
    # return the edge with the minimal cost
    minEdge = (None, None)
    if (len(edgeList) >= 1):
        minEdge = edgeList[0]
        minCost = dictOfEdge[edgeList[0]]
        for edge in edgeList:
            if (dictOfEdge[edge] <= minCost):
                minEdge = edge
                minCost = dictOfEdge[edge]
    return minEdge


def getEdgeThatContainsNodesOfT(Tnodes, Tedges, edgesGraph):
    edgeThatContainsNodesOfT = []
    for key1 in Tnodes:
        for key2 in edgesGraph:
            if int(key1) in key2:
                edgeThatContainsNodesOfT.append(key2)
    edgeThatContainsNodesOfT = list(set(edgeThatContainsNodesOfT))
   # print("edgeThatContainsNodesOfT : ")
   # print(edgeThatContainsNodesOfT)

    # and not in Tedges
    for edge in edgeThatContainsNodesOfT:
        if edge in Tedges:
            edgeThatContainsNodesOfT.remove(edge)
   # print("edgeThatContainsNodesOfT minus edge in Tedge : ")
   # print(edgeThatContainsNodesOfT)

    # the two nodes should not be in Tnode
    for edge in edgeThatContainsNodesOfT:
        a, b = edge
        if ((str(a) in Tnodes) and (str(b) in Tnodes)):
            edgeThatContainsNodesOfT.remove(edge)
   # print("edgeThatContainsNodesOfT minus 2 node in Tnodes : ")
   # print(edgeThatContainsNodesOfT)
    return edgeThatContainsNodesOfT


def adjustCost(Tnodes, Tedges, edgesGraph, nodeList):
    edgeThatContainsNodesOfT = getEdgeThatContainsNodesOfT(
        Tnodes, Tedges, edgesGraph)

    # recover the accessible node
    accessibleNode = []
    for edge in edgeThatContainsNodesOfT:
        if (str(edge[0]) not in Tnodes):
            accessibleNode.append(edge[0])
        if (str(edge[1]) not in Tnodes):
            accessibleNode.append(edge[1])
    accessibleNode = list(set(accessibleNode))

    # print(accessibleNode)

    for node in accessibleNode:
        tempEdgesList = []
        for edge in edgeThatContainsNodesOfT:
            if node in edge:
                tempEdgesList.append(edge)
        newCost = edgesGraph[shortestEdge(tempEdgesList, edgesGraph)]
        nodeList = editCostofNodeA(node, newCost, nodeList)

    return nodeList


def getCorrespondingEdge(Tnodes, nodeList, edgesGraph):
    if (len(nodeList) != 0):
        closestNode = min(nodeList)
        edgesTest = []
        a = int(closestNode[1])
        for node in Tnodes:
            b = int(node)

            if (a > b):
                edgesTest.append((b, a))
            elif (b < a):
                edgesTest.append((a, b))
    else:
        return

    # print("edgesTest")
    # print(edgesTest)

    CorrespondingEdge = shortestEdge(edgesTest, edgesGraph)

    # print("CorrespondingEdge")
    # print(CorrespondingEdge)

    return CorrespondingEdge


def printResolution(nodesG, edgesG, Tnodes, Tedges):
    print("Initial Graph : ")
    print(nodesG)
    print(edgesG)
    print("Soluce Graph : ")
    print(Tnodes)
    print(Tedges)


def primAlgorithmOnPoints(Graph):
    nodesGraph = Graph[0]
    edgesGraph = Graph[1]
    nodeList = createListOfNode(nodesGraph)
    Tnodes = {}
    Tedges = {}

    while (len(nodeList) > 0):

        minNode = getMinNode(nodeList)
        Tnodes[minNode[1]] = INFINITY  # first node added to T
        print("Sommet " + minNode[1] + " ajouté")
        # this node is removed of the nodeList
        nodeList = removeMinNode(nodeList)

        # Ajuster les coûts dans nodeList
        nodeList = adjustCost(Tnodes, Tedges, edgesGraph, nodeList)

        correspondingEdge = getCorrespondingEdge(Tnodes, nodeList, edgesGraph)
        if (correspondingEdge != None):
            Tedges[correspondingEdge] = edgesGraph[correspondingEdge]

    printResolution(nodesGraph, edgesGraph, Tnodes, Tedges)


listofProblems = read_problems(1, "Devoir_1/Code/Q3 ACM/input1.txt")


for problem in listofProblems:
    nodesGraph = initialisationOfNodes(problem)
    edgesGraph = initialisationOfEdges(problem)
    Graph = (nodesGraph, edgesGraph)

    primAlgorithmOnPoints(Graph)
