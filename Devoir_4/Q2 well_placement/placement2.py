from collections import deque

numero = 0
input_file = "input" + str(numero) + ".txt"


file = open(input_file, "r")
lines = file.readlines()
linesForResolution = []

"""# juste un print
for i in lines:
    print(i.strip())
file.close()
"""

line1 = (lines.pop(0).strip()).split(" ")
n = int(line1[0])
m = int(line1[1])

for i in lines:
    line = i.strip()
    row = []
    for j in line:
        row.append(int(j))
    linesForResolution.append(row)


def getNeighbor(matrix, v):
    n = len(matrix)
    m = len(matrix[0])
    i = v[0]
    j = v[1]
    neigh = []

    if j >= 0 and j <= m-2:
        # rigth
        neigh.append((i, j+1))
    if j >= 1 and j <= m-1:
        # left
        neigh.append((i, j-1))
    if i >= 0 and i <= n-2:
        # bottom
        neigh.append((i+1, j))
    if i >= 1 and i <= n-1:
        # top
        neigh.append((i-1, j))

    return neigh


def getFirstOne(matrix):
    find = True
    firstOne = (-1, -1)
    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 1 and find:
                firstOne = (i, j)
                find = False
    return firstOne


def dfsMod(matrix, v):
    stack = deque()
    stack.append(v)
    sizeOnes = 0

    while len(stack) != 0:
        v = stack.pop()

        i = v[0]
        j = v[1]

        if matrix[i][j] == 2:
            continue

        if matrix[i][j] != 2:
            sizeOnes += 1
            matrix[i][j] = 2

        neigh = getNeighbor(matrix, v)

        for neighbor in neigh:
            if matrix[neighbor[0]][neighbor[1]] == 1:
                stack.append(neighbor)
            else:
                matrix[neighbor[0]][neighbor[1]] = 2

    return matrix, sizeOnes


v = getFirstOne(linesForResolution)
maximum = 0

if v == (-1, -1):
    pass
else:
    for i in range(0, n):
        for j in range(0, m):
            if (linesForResolution[i][j] == 1):
                linesForResolution, potmax = dfsMod(linesForResolution, (i, j))
                if potmax > maximum:
                    maximum = potmax

print(maximum)
