import time
import math
INFINITY = math.inf


def read_problems(problems, input_file):
    # lecture du fichier/file reading
    path = "Devoir_1/Code/Q3 ACM/" + input_file
    file = open(path, "r")
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


listofProblems = read_problems(
    1, "input7.txt")


def distanceBetweenTwoCoordinate(coor1, coor2):
    return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**(1/2)


class Node:
    def __init__(self, node, cost):
        self._node = node
        self._parent = self
        self._cost = cost

    def get_Parent(self):
        return self._parent

    def get_Node(self):
        return self._node

    def get_Cost(self):
        return self._cost

    def set_Parent(self, newParent):
        self._parent = newParent

    def set_Cost(self, newCost):
        self._cost = newCost

    def print(self):
        print(f"node : {self._node}, parent's node {self._parent._node} ")

    def __lt__(self, other):
        return self._cost < other._cost

    def __le__(self, other):
        return self._cost <= other._cost

    def __gt__(self, other):
        return self._cost > other._cost

    def __ge__(self, other):
        return self._cost >= other._cost


def prim_array(ListOfProblems):

    string = ""

    for problem in ListOfProblems:
        # Initialisation Matrix of cost
        matrixOfCost = []
        for i in range(0, len(problem)):
            row = []
            for j in range(0, len(problem)):
                ci = problem[i]
                cj = problem[j]
                if (i < j):
                    row.append(distanceBetweenTwoCoordinate(ci, cj))
                else:
                    row.append(0)
            matrixOfCost.append(row)

        for i in range(0, len(problem)):
            matrixOfCost[i][i] = 0
            for j in range(0, len(problem)):
                if (i < j):
                    matrixOfCost[j][i] = matrixOfCost[i][j]

        # Initialisation list of nodes
        listOfNode = []
        for i in range(1, len(problem)):
            listOfNode.append(Node(i, INFINITY))
        listOfNode.append(Node(0, 0))

        Tcost = 0
        # Prim algorithm with a array
        while len(listOfNode) > 0:

            minNode = min(listOfNode)
            Tcost += matrixOfCost[minNode.get_Parent().get_Node()
                                  ][minNode.get_Node()]
            listOfNode.remove(minNode)

            for node in listOfNode:
                costUandAdjacent = matrixOfCost[minNode.get_Node(
                )][node.get_Node()]
                if (costUandAdjacent < node.get_Cost()):
                    node.set_Parent(minNode)
                    node.set_Cost(costUandAdjacent)
        # print(round(Tcost, 3))
        string += (f"{round(Tcost, 3)}\n")
    print(string)
    pass


start = time.time()
prim_array(listofProblems)
print(time.time() - start)


def write(fileName, content):
    # écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()
