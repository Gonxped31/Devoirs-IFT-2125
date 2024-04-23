import math


numero = 1
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

dictConflict = {student: [] for student in students}
for pair in pairs:
    student1, student2 = pair
    dictConflict[student1].append(student2)
    dictConflict[student2].append(student1)


def backTrackingGroupSeparation(group1, group2, dictionnary):

    if len(group2) == 0:
        return

    if len(group1) == 0:
        actualStudent = group2[0]
        group1.append(actualStudent)
        group2.remove(actualStudent)
        return backTrackingGroupSeparation(group1, group2, dictionnary)

    next = True

    for i in group2:
        for j in group1:
            if i in dictConflict[j]:
                next = False
                break
        if (next):
            group1.append(i)
            group2.remove(i)
            if len(group1) >= math.ceil((len(dictionnary))/2):

                for k in group2:
                    for l in group2:
                        if l in dictionnary[k]:
                            return

                return group1, group2
            return backTrackingGroupSeparation(group1, group2, dictionnary)
        next = True


result = backTrackingGroupSeparation([], students, dictConflict)
bigString = ""
if result == None:
    bigString += "impossible"
elif (len(result) == 2):
    for i in range(len(result[0])):
        bigString += str(result[0][i]) + " "
    bigString += "\n"
    for i in range(len(result[1])):
        bigString += str(result[1][i]) + " "

for key, value in dictConflict.items():
    print(key, ":", value)

print(bigString)
