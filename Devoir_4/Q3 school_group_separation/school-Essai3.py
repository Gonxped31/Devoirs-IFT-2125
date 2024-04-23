import math
from collections import deque
import time


numero = 6
input_file = "input" + str(numero) + ".txt"

# lecture du fichier
fileIn = open(input_file, "r")
linesIn = fileIn.readlines()
fileIn.close()

nbStudents = int(linesIn[0])
students = []
if (nbStudents != 0):
    students = [s.strip() for s in linesIn[1:nbStudents+1]]
nbPairs = int(linesIn[nbStudents+1])
pairs = []
if (nbPairs != 0):
    pairs = [s.strip().split()
             for s in linesIn[nbStudents+2:nbStudents+nbPairs+2]]

# print(students)
# print(pairs)

dictionnary = {student: [] for student in students}
for pair in pairs:
    student1, student2 = pair
    dictionnary[student1].append(student2)
    dictionnary[student2].append(student1)

"""for key, value in dictionnary.items():
    print(key, ":", value)"""

debut = time.time()
soluce = []
group1 = set([])
group2 = set([])
forbidden = set([])
next = True
listOfKeys = list(dictionnary.keys())

for key in dictionnary:
    if (next):
        if key not in group1 and key not in forbidden:
            group1.add(key)
            listOfKeys.remove(key)
            forbidden = forbidden.union(set(dictionnary[key]))

            if len(group1) >= math.ceil((len(dictionnary))/2):
                group2 = listOfKeys
                next = False
                for k in group2:
                    for l in group2:
                        if l in dictionnary[k]:
                            soluce = None
                soluce = (list(group1), group2)

# -------------------------------
fin = time.time()
duree = fin - debut
print(f"algo terminé : {duree} secondes, file : {numero}")
# -------------------------------


def backTrackingGroupSeparation(group1, group2, dictionnary):

    Stack = []

    if len(group2) == 0:
        return

    if len(group1) == 0:
        actualStudent = group2[0]
        group1.append(actualStudent)
        group2.remove(actualStudent)
        Stack.append((group1, group2, 0))
        # print(Stack)

    goodOne = True

    while (len(Stack) != 0):

        group1, group2, index = Stack.pop()

        candidate = group2[index]
        """print(f"candidate : {candidate}")
        print(f"groupe 1 : {group1}")
        print(f"groupe 2 : {group2}")"""

        for i in group1:
            if candidate in dictionnary[i]:
                goodOne = False
                break

        if (not goodOne):
            index += 1
            if index < len(group2):
                Stack.append((group1, group2, index))
        else:
            # print(candidate)
            Stack.append((group1, group2, index))
            group1.append(candidate)
            group2.remove(candidate)
            """print(f"groupe 1 : {group1}")
            print(f"groupe 2 : {group2}\n")"""
            Stack.append((group1, group2, 0))

        if len(group1) >= math.ceil((len(dictionnary))/2):
            for k in group2:
                for l in group2:
                    if l in dictionnary[k]:
                        return
            return group1, group2

        goodOne = True


# result = backTrackingGroupSeparation([], students, dictionnary)
result = soluce

bigString = ""
if result == None:
    bigString += "impossible"
elif (len(result) == 2):
    for i in range(len(result[0])):
        bigString += str(result[0][i]) + " "
    bigString += "\n"
    for i in range(len(result[1])):
        bigString += str(result[1][i]) + " "


# print(bigString)
