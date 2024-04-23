
import math
import random
import time


def millerRabinPrimalityTest(n):
    if n < 2047:
        optValue = [2]
    elif n < 1373653:
        optValue = [2, 3]
    elif n < 9080191:
        optValue = [31, 73]
    elif n < 25326001:
        optValue = [2, 3, 5]
    elif n < 3215031751:
        optValue = [2, 3, 5, 7]
    elif n < 4759123141:
        optValue = [2, 7, 61]
    elif n < 1122004669633:
        optValue = [2, 13, 23, 1662803]

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    s = 0
    t = n-1
    y = 0

    while (t % 2 == 0):
        s += 1
        t = t//2

    for i in optValue:
        a = i
        x = pow(a, t, n)
        for j in range(0, s):
            y = (x**2) % n
            if y == 1 and x != 1 and x != n-1:
                return False
            x = y
        if y != 1:
            return False
    return True


def verifySpecialEnsemble(tab):
    for i in range(0, len(tab)):
        for j in range(i+1, len(tab)):
            if millerRabinPrimalityTest((int(str(tab[i])+str(tab[j])))) and millerRabinPrimalityTest((int(str(tab[j])+str(tab[i])))):
                pass
            else:
                return False
    return True


# print(verifySpecialEnsemble([3, 5, 7, 11]))

def findSpecial(primeNumber, start, end):
    soluce = []
    for i in range(start, end, -1):
        for j in range(i-1, - 1, -1):
            if verifySpecialEnsemble([primeNumber[i], primeNumber[j]]):
                for k in range(j-1, - 1, -1):
                    if verifySpecialEnsemble([primeNumber[i], primeNumber[k]]) and verifySpecialEnsemble([primeNumber[j], primeNumber[k]]):
                        for l in range(k-1, - 1, -1):
                            if verifySpecialEnsemble([primeNumber[i], primeNumber[l]]) and verifySpecialEnsemble([primeNumber[j], primeNumber[l]]) and verifySpecialEnsemble([primeNumber[k], primeNumber[l]]):
                                soluce.append(
                                    sum([primeNumber[i], primeNumber[j], primeNumber[k], primeNumber[l]]))
    return soluce


def write(fileName, content):
    Outputfile = open(fileName, "w")
    Outputfile.write(content)
    Outputfile.close()


"""M = 50

primeNumber = []
lastSize = 1000
nextNumber = 3

debut = time.time()

while len(primeNumber) < lastSize:
    if (millerRabinPrimalityTest(nextNumber)):
        primeNumber.append(nextNumber)
    nextNumber += 1

print(f" last prime ( {lastSize} ) = {nextNumber-1}")

fin = time.time()
duree = fin - debut
print(f"Total recherche nb prime : {duree} secondes")

soluce = []

debut = time.time()
soluce = findSpecial(primeNumber, len(primeNumber)-1, -1)
# soluce = findSpecial(primeNumber, 300, 2)

soluce = []
start = len(primeNumber)-1
end = -1
for i in range(start, end, -1):
    for j in range(i-1, - 1, -1):
        if verifySpecialEnsemble([primeNumber[i], primeNumber[j]]):
            for k in range(j-1, - 1, -1):
                if verifySpecialEnsemble([primeNumber[i], primeNumber[k]]) and verifySpecialEnsemble([primeNumber[j], primeNumber[k]]):
                    for l in range(k-1, - 1, -1):
                        if verifySpecialEnsemble([primeNumber[i], primeNumber[l]]) and verifySpecialEnsemble([primeNumber[j], primeNumber[l]]) and verifySpecialEnsemble([primeNumber[k], primeNumber[l]]):
                            soluce.append(
                                sum([primeNumber[i], primeNumber[j], primeNumber[k], primeNumber[l]]))"""

"""raising = (math.log10(M))**2

while len(soluce) < (raising*M):
    previousLastSize = lastSize
    lastSize = 2*lastSize
    while len(primeNumber) < lastSize:
        if (millerRabinPrimalityTest(nextNumber)):
            primeNumber.append(nextNumber)
        nextNumber += 1
    print(f" last prime ( {lastSize} ) = {nextNumber-1}")
    newSoluce = findSpecial(primeNumber, len(
        primeNumber)-1, previousLastSize-1)
    for i in newSoluce:
        soluce.append(i)
"""

"""
fin = time.time()
duree = fin - debut
print(f"Total recherche special 4 : {duree} secondes")


soluce = sorted(soluce)

bigString = ""
ind = 1
for s in soluce:
    bigString += f" tab {ind} : {s} \n"
    ind += 1


write("recherche.txt", f"Total recherche special 4 : {duree} secondes\n")
write("recherche.txt", bigString)
"""


"""def isprime(n, k=80):
    # Common optValue for deterministic testing below certain thresholds
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^s * d where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # List of optValue for deterministic version based on n's range
    if n < 2047:
        optValue = [2]
    elif n < 1373653:
        optValue = [2, 3]
    elif n < 9080191:
        optValue = [31, 73]
    elif n < 25326001:
        optValue = [2, 3, 5]
    elif n < 3215031751:
        optValue = [2, 3, 5, 7]
    elif n < 4759123141:
        optValue = [2, 7, 61]
    elif n < 1122004669633:
        optValue = [2, 13, 23, 1662803]
    else:
        # Using 80 random optValue for very large n; adjust as needed
        optValue = [int(random.uniform(2, n-2)) for in range(k)]

    # Miller-Rabin test using the selected optValue
    for a in optValue:
        x = pow(a, d, n)
        if x in (1, n-1):
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True"""


def findNthSpecial4PrimeNumber(N, lastSize=2):
    primeNumber = []
    nextNumber = 3

    while len(primeNumber) < lastSize:
        if (millerRabinPrimalityTest(nextNumber)):
            primeNumber.append(nextNumber)
        nextNumber += 2

    soluce = findSpecial(primeNumber, len(primeNumber)-1, -1)
    # raising = math.ceil((math.log2(N)))

    while len(soluce) < 5*N:
        previousLastSize = lastSize
        # lastSize = int(((math.log10(N))**2)*lastSize)
        lastSize = lastSize + 1
        # print(f" new one : {lastSize}")
        while len(primeNumber) < lastSize:
            if (millerRabinPrimalityTest(nextNumber)):
                primeNumber.append(nextNumber)
            nextNumber += 2

        newSoluce = findSpecial(primeNumber, len(
            primeNumber)-1, previousLastSize-1)
        for i in newSoluce:
            soluce.append(i)
    print(f"\n needed ----> {lastSize}")
    soluce = sorted(soluce)
    return soluce[N-1]


tabfinal = [1, 2, 3, 6, 15, 25, 50, 100]

N = 50

debut = time.time()

soluce = findNthSpecial4PrimeNumber(N)
print(f" {N} ieme : {soluce}")

fin = time.time()
duree = fin - debut
print(f" time = {duree}")

# ind = 1
"""for i in soluce:
    print(f" {ind} eme : {i}")
    ind += 1"""
