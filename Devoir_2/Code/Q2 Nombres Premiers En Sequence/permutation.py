

import math


"""print(f"Entre 100 et 999 :  {btwn100_999} ")
print(f"Entre 1000 et 9999 :  {btwn1000_9999} ")"""


def splitNumber(number):
    tabNumber = []
    for i in range(0, len(str(number))):
        tabNumber.append(int(str(number)[i]))
    return tabNumber


print(splitNumber(95))

base10Numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

permutate = []

for i in range(0, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            permutate.append(base10Numbers[i] +
                             base10Numbers[j]+base10Numbers[k])


"""

doubleResult = []
for i in result:
    doubleResult.append(permutOneBoucle(["a", "b"], 1, i))

print(doubleResult)"""


"""result1 = []
for i in tab:
    result1.append(i)


result2 = []
for j in tab:
    for i in result1:
        result2.append(i + j)


result3 = []
for j in tab:
    for i in result2:
        result3.append(i + j)

print(result3)"""


def permutTOTAL(tab, result=[""]):
    if len(tab) == 1:
        return tab
    else:
        resultBis = []
        for j in tab:
            for i in result:
                resultBis.append(i + j)
        if len(resultBis[0]) == len(tab):
            return resultBis
        else:
            return permutTOTAL(tab, resultBis)


# print(permutTOTAL(["0", "1", "2"]))


tabAB = ["a", "b"]


def biPermut(tab):
    result = []
    if len(tab) == 2:
        result.append(str(tab[0])+str(tab[1]))
        result.append(str(tab[1])+str(tab[0]))
    return result


print(biPermut(tabAB))

tabOriginale = ["1", "1", "2"]

result = []
for i in tabOriginale:
    tabCopie = tabOriginale[:]
    tabCopie.remove(i)
    for j in tabCopie:
        tabCopie1 = tabCopie[:]
        tabCopie1.remove(j)
        for k in tabCopie1:
            tabCopie2 = tabCopie1[:]
            tabCopie2.remove(k)
            result.append(i+j+k)


# print(set(result))

# print(splitNumber(11348))

def printTableau(tab):
    for i in tab:
        print(i)


def codePermut(number):
    numOccurenrence = []
    for i in range(0, 10):
        numOccurenrence.append(0)
    numTab = splitNumber(number)
    for j in numTab:
        numOccurenrence[j] = numOccurenrence[j] + 1
    code = ""
    for k in numOccurenrence:
        code += str(k)
    return code


# print(codePermut(115))
# print(codePermut(511))


primeNumber = []
number = 10000

for i in range(0, number + 1):
    primeNumber.append(1)


for i in range(2, int(math.sqrt(number)+1)):
    if (primeNumber[i] == 1):
        for j in range(i+1, number):
            if (j % i == 0):
                primeNumber[j] = 0


premier = []
for i in range(2, len(primeNumber)):
    if (primeNumber[i] == 1):
        premier.append(i)

# printTableau(premier)
# printTableau(premier[0:32])
# print(len((premier)))

"""b-a = c-b
2b = c+a 
c = 2b - a"""

potentiel = []

for i in range(0, len(premier)):

    if (i % 200 == 0):
        print("je roule")

    for j in range(i+1, len(premier)):

        if (codePermut(premier[i]) != codePermut(premier[j])):
            continue

        c = 2*premier[j]-premier[i]

        if (codePermut(c) != codePermut(premier[j])):
            continue

        if c in premier:
            potentiel.append([premier[i], premier[j], c])

print(potentiel)
