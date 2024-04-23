from collections import deque


numero = 0
input_file = "input" + str(numero) + ".txt"
tabstr = ""

file = open(input_file, "r")
lines = file.readlines()
for i in lines:
    print(i.strip())
file.close()

print("longstr ready")


line1 = (lines.pop(0).strip()).split(" ")
n = int(line1[0])
m = int(line1[1])
# print(n, m)

for i in lines:
    line = i.strip()
    for j in line:
        tabstr += str(j)
# print(tabstr)


class Node():
    def __init__(self, number) -> None:
        self.number = number
        self.status = False

    def getNumber(self):
        return self.number

    def setNumber(self, newNumber):
        self.number = newNumber
        return

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus
        return


class Graphe():
    def __init__(self, n, m, longstr) -> None:
        self.n = n
        self.m = m
        allNodes = []
        for i in range(0, n*m):
            allNodes.append(Node(int(longstr[i])))
            """if (i % n*m == 2000):
                print(f"En cours i = +{i} ")"""
        self.allNodes = allNodes

    def getAllNodes(self):
        return self.allNodes

    def getNumber(self, i):
        return self.allNodes[i].getNumber()

    def getStatus(self, i):
        return self.allNodes[i].getStatus()

    def setNumber(self, i, newNumber):
        self.allNodes[i].setNumber(newNumber)
        return

    def setStatus(self, i, newStatus):
        self.allNodes[i].setStatus(newStatus)
        return

    def fillNumber(self, longStr):
        if len(longStr) != (self.n)*(self.m):
            return

        for i in range(0, (self.n)*(self.m)):
            self.setNumber(i, int(tabstr[i]))

        return

    def getNeighbor(self, i):
        n = self.n
        m = self.m
        neighbors = []

        if (i < 0 or i >= self.n*self.m):
            return

        if m == 1:
            if i == 0:
                neighbors = [i+1]
            elif i == n-1:
                neighbors = [i-1]
            else:
                neighbors = [i+1, i-1]
            return neighbors

        if n == 1:
            if i == 0:
                neighbors = [i+1]
            elif i == m-1:
                neighbors = [i-1]
            else:
                neighbors = [i+1, i-1]
            return neighbors

        if (n > 1 and m > 1):
            if (i == 0):
                neighbors = [1, m]
            elif (i == m-1):
                neighbors = [i-1, i+m]
            elif (i == m*(n-1)):
                neighbors = [i-m, i+1]
            elif (i == m*n-1):
                neighbors = [i-1, i-m]
            elif (i % m != 0 and i % m != m-1 and i//m != 0 and i//m != n-1):
                neighbors = [i+1, i-1, i+m, i-m]
            elif (i % m == 0):
                neighbors = [i+1, i+m, i-m]
            elif (i % m == m-1):
                neighbors = [i-1, i+m, i-m]
            elif (i // m == 0):
                neighbors = [i+1, i-1, i+m]
            elif (i // m == n-1):
                neighbors = [i+1, i-1, i-m]
        return neighbors

    def getfirstOne(self):
        for i in range(0, n*m):
            if self.getNumber(i) == 1:
                return i
        return n*m


"""verif = ""
for i in range(0, n*m):
    verif += str(g.getNumber(i))
print(verif)"""


"""neigh = g.getNeighbor(7)
print(neigh)"""

"""v = g.getfirstOne()

if v == n*m:
    print("pas de 1")
else:
    print("suite")


stack = deque()
stack.append(v)

while len(stack) != 0:
    v = stack.pop()

    if g.getStatus(v):
        continue

    if not g.getStatus(v):
        print(v)
        g.setStatus(v, True)

    neigh = g.getNeighbor(v)

    for i in neigh:
        if g.getNumber(i) == 1:
            stack.append(i)
        else:
            g.setStatus(i, True)"""


def dfsMod(g, v):
    stack = deque()
    stack.append(v)
    sizeOnes = 0

    while len(stack) != 0:
        v = stack.pop()

        if g.getStatus(v):
            continue

        if not g.getStatus(v):
            sizeOnes += 1
            g.setStatus(v, True)

        neigh = g.getNeighbor(v)

        for i in neigh:
            if g.getNumber(i) == 1:
                stack.append(i)
            else:
                g.setStatus(i, True)
    return g, sizeOnes


g = Graphe(n, m, tabstr)
print("filling finish")

v = g.getfirstOne()
max = 0

if v == n*m:
    pass
else:
    for i in range(0, n*m):
        if (not g.getStatus(i)) and (g.getNumber(i) == 1):
            g, potmax = dfsMod(g, i)
            if potmax > max:
                print(max)
                max = potmax

print(max)
