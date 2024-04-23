# Gbian Bio Samir, 20250793
# Sourou Johann, 20227958

import sys


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


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


def findNthSpecial4PrimeNumber(N, lastSize=2):
    primeNumber = []
    nextNumber = 3

    while len(primeNumber) < lastSize:
        if (millerRabinPrimalityTest(nextNumber)):
            primeNumber.append(nextNumber)
        nextNumber += 2

    soluce = findSpecial(primeNumber, len(primeNumber)-1, -1)

    while len(soluce) < 5*N:
        previousLastSize = lastSize
        lastSize = lastSize + 1
        while len(primeNumber) < lastSize:
            if (millerRabinPrimalityTest(nextNumber)):
                primeNumber.append(nextNumber)
            nextNumber += 2

        newSoluce = findSpecial(primeNumber, len(
            primeNumber)-1, previousLastSize-1)
        for i in newSoluce:
            soluce.append(i)
    soluce = sorted(soluce)
    return soluce[N-1]


def main(args):
    n = int(args[0])
    output_file = args[1]
    answer = findNthSpecial4PrimeNumber(n)
    # answering
    write(output_file, str(answer))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
