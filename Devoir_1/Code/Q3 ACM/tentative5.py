import time
import math
import heapq
INFINITY = math.inf
start_timeFinal = time.time()


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


listofProblems = read_problems(1, "Devoir_1/Code/Q3 ACM/input7.txt")
firstProblem = listofProblems[0]


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
        self._parent = newCost

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


start_time = time.time()

matrixOfCost = []
for i in range(0, len(firstProblem)):
    row = []
    for j in range(0, len(firstProblem)):
        ci = firstProblem[i]
        cj = firstProblem[j]
        if (i < j):
            row.append(distanceBetweenTwoCoordinate(ci, cj))
        else:
            row.append(0)
    matrixOfCost.append(row)

for i in range(0, len(firstProblem)):
    matrixOfCost[i][i] = 0
    for j in range(0, len(firstProblem)):
        if (i < j):
            matrixOfCost[j][i] = matrixOfCost[i][j]

print("--- %s seconds --- : intialisation  " % (time.time() - start_time))

heapOfNode = []
heapq.heapify(heapOfNode)
for i in range(1, len(firstProblem)):
    heapq.heappush(heapOfNode, Node(i, INFINITY))
heapq.heappush(heapOfNode, Node(0, INFINITY))

start_time = time.time()
Tcost = 0

while len(heapOfNode) > 0:

    newHeapOfNode = []
    heapq.heapify(newHeapOfNode)

    minNode = heapq.heappop(heapOfNode)
    Tcost += matrixOfCost[minNode.get_Parent().get_Node()][minNode.get_Node()]

    for node in heapOfNode:

        costUandAdjacent = matrixOfCost[minNode.get_Node()][node.get_Node()]
        nodeName = node.get_Node()

        if (costUandAdjacent < node.get_Cost()):
            newNode = Node(nodeName, costUandAdjacent)
            newNode.set_Parent(minNode)
            heapq.heappush(newHeapOfNode, newNode)
        else:
            heapq.heappush(newHeapOfNode, node)

    heapOfNode = newHeapOfNode

print("--- %s seconds --- : Algorithm  " % (time.time() - start_time))

print(Tcost)

print("--- %s seconds Total ---" % (time.time() - start_timeFinal))
