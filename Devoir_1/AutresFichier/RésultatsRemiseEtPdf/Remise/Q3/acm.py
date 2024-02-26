# Gbian Bio Samir, 20250793
# Sourou Johann, 20227958

import math
import sys
INFINITY = math.inf

# Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier,
# faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
# d'autres librairies.
# Functions to read/write in files. you can modify them, do some parsing,
# add a return value, but don't use other librairies


def read_problems(input_file):
    # lecture du fichier/file reading
    path = "Devoirs-IFT-2125/Devoir_1/Code/Q3 ACM/" + input_file
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


def prim_priority_quue():
    pass

# Prim algorithm implemented with array (for hight density)


def prim_array(ListOfProblems):

    string = ""
    for problem in ListOfProblems:
        # Initialisation Matrix of cost
        matrixOfCost = matrixCostForAproblem(problem)

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
    return string


def read_problems(input_file):

    # lecture du fichier/file reading
    path = input_file
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


def distanceBetweenTwoCoordinate(coor1, coor2):
    return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**(1/2)


def matrixCostForAproblem(problem):
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

    return matrixOfCost


def write(fileName, content):
    # écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()

# Fonction main/Main function


def main(args):
    input_file = args[0]
    output_file = args[1]
    string = prim_array(read_problems(input_file))
    write(output_file, string)

# Kruskal algorithm (for low density)


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
