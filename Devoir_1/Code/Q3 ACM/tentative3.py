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


listofProblems = read_problems(1, "Devoir_1/Code/Q3 ACM/input4.txt")

firstProblem = listofProblems[0]
# print(firstProblem)

print("--- %s Problem 1 --- :\n")


def inComposante(listOfEdge, node):
    for edge in listOfEdge:
        if (node in edge) or (node == edge):
            return True
    return False


def distanceBetweenTwoCoordinate(coor1, coor2):
    return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**(1/2)


# print(distanceBetweenTwoCoordinate(firstProblem[0], firstProblem[1]))

def composanteOF(listOfComposante, node):
    for composante in listOfComposante:
        if node in composante:
            return composante
    return


def sameComposante(listOfComposante, nodeA, nodeB):
    for composante in listOfComposante:
        if (nodeA in composante) and (nodeB in composante):
            return True
    return False


def fusionComposante(ListOfComposante, nodeA, nodeB):
    compA = composanteOF(ListOfComposante, nodeA)
    compB = composanteOF(ListOfComposante, nodeB)
    c = compA.union(compB)
    ListOfComposante.remove(compA)
    ListOfComposante.remove(compB)
    ListOfComposante.append(c)
    return ListOfComposante


listOfEdge = []
start_time = time.time()
for i in range(0, len(firstProblem)):
    for j in range(0, len(firstProblem)):
        ci = firstProblem[i]
        cj = firstProblem[j]
        if (i < j):
            listOfEdge.append((distanceBetweenTwoCoordinate(ci, cj), (i, j)))
# for edge in listOfEdge:
   # print(edge)
print("--- %s seconds --- : Initaliser list of edge with cost " %
      (time.time() - start_time))


connectedNode = []
total = 0

start_time = time.time()
composanteTab = []
for i in range(0, len(firstProblem)):
    a = set({i})
    composanteTab.append(set(a))
print("--- %s seconds --- : Initaliser composante " %
      (time.time() - start_time))

# print(composanteTab)
# composante is a table with  edges and nodes

Testtt = []

i = 0
start_time = time.time()
while (len(listOfEdge) > 0):
    soluceEdege = []
    couple = min(listOfEdge)
    cost = couple[0]
    edge = couple[1]
    if (not sameComposante(composanteTab, edge[0], edge[1])):
        composanteTab = fusionComposante(composanteTab, edge[0], edge[1])
        Testtt.append((edge[0], edge[1]))
        total += cost
    listOfEdge.remove(couple)
    """if (i % 100 == 1):
        print(cost)
    i += 1"""
print("--- %s seconds --- : Algorithm " % (time.time() - start_time))


print("\nSOLUCE :")
print(Testtt)
print(total)


print("--- %s seconds ---" % (time.time() - start_timeFinal))


def intru(tab1, tab2):
    print(f"  tab1 : {len(tab1)}")
    print(f"  tab2 : {len(tab2)}")
    # print(f"  tab1 : {tab1}")
    # print(f"  tab2 : {tab2}")
    tab1prime = []
    tab2prime = []
    intersection = []
    tab2WithoutIntersection = []
    tab2ShouldBeContain = []

    for couple in tab1:
        a = set(couple)
        tab1prime.append(a)
    print(tab1prime)

    for couple in tab2:
        b = set(couple)
        tab2prime.append(b)
    print(tab2prime)

    for A in tab1prime:
        if A in tab2prime:
            intersection.append(set(A))

    print(f"  INTERSECTION : {intersection}")

    for A in tab2prime:
        if A not in intersection:
            tab2WithoutIntersection.append(set(A))

    print(f"  tab 2 without INTERSECTION : {tab2WithoutIntersection}")

    for A in tab1prime:
        if A not in intersection:
            tab2ShouldBeContain.append(set(A))
    print(f"  tab 2 should be contain : {tab2ShouldBeContain}")

    return


"""


stop



"""

firstProblem = listofProblems[0]


def distanceBetweenTwoCoordinate(coor1, coor2):
    return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**(1/2)


class Node:
    def __init__(self, node):
        self._node = node
        self._parent = self

    def get_Parent(self):
        return self._parent

    def set_Parent(self, newParent):
        self._parent = newParent

    def print(self):
        print(f"node : {self._node}, parent's node {self._parent._node} ")

    def get_Node(self):
        return self._node


heapOfLabel = []
listOfNode = []
heapq.heapify(heapOfLabel)

heapq.heappush(heapOfLabel, (0, 0))
listOfNode.append(Node(0))

for i in range(1, len(firstProblem)):
    listOfNode.append(Node(i))
    heapq.heappush(heapOfLabel, (INFINITY, i))

# listOfNode[0].print()

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
for rowCost in matrixOfCost:
    print(rowCost)

# T is a tab of edges
# Tcost is the answer

T = []
Tcost = 0
n = 0

start_time = time.time()

while len(heapOfLabel) > 0:

    """n += 1
    if (n % 100 == 0):
        print(len(heapOfLabel))"""

    print("###")

    # (cost, node)
    labelMin = heapq.heappop(heapOfLabel)
    nodeMin = listOfNode[labelMin[1]]

    T.append((nodeMin.get_Parent().get_Node(), nodeMin.get_Node()))
    Tcost += matrixOfCost[nodeMin.get_Parent().get_Node()][nodeMin.get_Node()]
    print(
        f" cost += {matrixOfCost[nodeMin.get_Parent().get_Node()][nodeMin.get_Node()]}")

    label = labelMin[0]
    # print(label)
    listOfPush = []
    listOfRemove = []

    # print(heapOfLabel)

    print(f"edge p : {nodeMin.get_Node()}")

    for heap in heapOfLabel:

        costUandAdjacent = matrixOfCost[nodeMin.get_Node()][heap[1]]

        """print(f"\ncostUandAdjacent : {costUandAdjacent}")
        print(f"heap : {heap}")
        print(f"edge : {heap[1]}")"""

        costPlace = heap[1]

        if (costUandAdjacent < heap[0]):
            listOfRemove.append(heap)
            listOfPush.append((costUandAdjacent, costPlace))
            listOfNode[costPlace].set_Parent(nodeMin)

    for push in listOfPush:
        heapq.heappush(heapOfLabel, push)
        print(f" New heap : {(push)}")

    for remove in listOfRemove:
        heapOfLabel.remove(remove)
        print(f" Ancien heap : {(remove)}")
print("--- %s seconds --- : Algorithm " % (time.time() - start_time))


print(f" \n   heapOfLabel : {heapOfLabel}")

print(f"\n{T}")
print(Tcost)

print("--- %s seconds Total ---" % (time.time() - start_timeFinal))


print(f" GROS PRINT : {intru(Testtt, T)}")
