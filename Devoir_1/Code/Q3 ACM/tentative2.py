import time
import math
INFINITY = math.inf
start_time = time.time()


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


listofProblems = read_problems(1, "Devoir_1/Code/Q3 ACM/input3.txt")

firstProblem = listofProblems[0]
# print(firstProblem)


def distanceBetweenTwoCoordinate(coor1, coor2):
    return ((coor1[0]-coor2[0])**2 + (coor1[1]-coor2[1])**2)**(1/2)


# print(distanceBetweenTwoCoordinate(firstProblem[0], firstProblem[1]))

"""matrix = []

for i in range(0, len(firstProblem)):
    row = []
    for j in range(0, len(firstProblem)):
        if (i < j):
            row.append((i, j))
        else:
            row.append((0, 0))
    matrix.append(row)

for row in matrix:
    print(row)

print("Matrice N O W")"""

matrix = []

for i in range(0, len(firstProblem)):
    row = []
    for j in range(0, len(firstProblem)):
        ci = firstProblem[i]
        cj = firstProblem[j]
        if (i < j):
            row.append(distanceBetweenTwoCoordinate(ci, cj))
        else:
            row.append(INFINITY)
    matrix.append(row)

# for row in matrix:
   # print(row)

"""
print("(3-4)")
print(distanceBetweenTwoCoordinate(firstProblem[3], firstProblem[4]))

print("(3-1)")
print(distanceBetweenTwoCoordinate(firstProblem[3], firstProblem[1]))

print("(0-4)")
print(distanceBetweenTwoCoordinate(firstProblem[0], firstProblem[4]))

print("(0-1)")
print(distanceBetweenTwoCoordinate(firstProblem[0], firstProblem[1]))
"""


edgesSoluce = []

for i in range(0, len(firstProblem) - 2):
    # print("hey : " + str(i+1))
    row = matrix[i]
    minValue = min(row)
    find = True
    for j in range(0, len(firstProblem)):
        if (i < j):
            if (minValue == row[j]) and find:
                edgesSoluce.append((i, j))
                # print("(" + str(i) + ", " + str(j) + ")")
                find = False
        else:
            pass
    matrix.append(row)

n = len(firstProblem)-1
minValueLastEdge = INFINITY
minEdges = (None, None)

for i in range(0, len(firstProblem)):
    for j in range(0, len(firstProblem)):
        """ 
        print("i,j : " + str((i, j)))
        print("n == j : " + str(n == j))
        print("matrix[i][j] <= minValue : " + str((matrix[i][j] <= minValue)) +
              ", min Value = " + str(minValueN) + ", matrix[i][j] = " + str(matrix[i][j]))
        print("(i, j) not in edgesSoluce : " + str((i, j) not in edgesSoluce))
        print("\n")
        """
        if (n == j and (matrix[i][j] <= minValueLastEdge) and ((i, j) not in edgesSoluce)):
            minValueLastEdge = matrix[i][j]
            minEdges = (i, j)

edgesSoluce.append(minEdges)
total = 0

for edge in edgesSoluce:
    total += matrix[edge[0]][edge[1]]

print("SOLUCE : \n")

print(total)

print("--- %s seconds ---" % (time.time() - start_time))
