# Gbian Bio Samir, 20250793
# Sourou Johann, 20227958

import sys
import time
from collections import deque


def read_problem(MyGraph="", input_file="input.txt"):

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    linesForResolution = []
    lines.pop(0)

    for i in lines:
        line = i.strip()
        row = []
        for j in line:
            row.append(int(j))
        linesForResolution.append(row)

    return linesForResolution


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
    n = len(matrix)
    m = len(matrix[0])
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


def write(fileName, content):
    # write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    debut = time.time()

    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    matrix = read_problem(input_file=input_file)
    n = len(matrix)
    m = len(matrix[0])

    v = getFirstOne(matrix)
    answer = 0
    if v == (-1, -1):
        pass
    else:
        for i in range(0, n):
            for j in range(0, m):
                if (matrix[i][j] == 1):
                    matrix, potmax = dfsMod(matrix, (i, j))
                    if potmax > answer:
                        answer = potmax
    print(answer)
    # answering
    write(output_file, str(answer))

    fin = time.time()
    duree = fin - debut
    print(f"Durée d'exécution : {duree} secondes")


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
