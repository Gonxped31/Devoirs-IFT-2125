# Nom, matricule
# Nom, matricule

# Fonction à compléter. Ne modifiez pas sa signature.
# N : Force maximale
# k : Nombre de fenêtres disponibles
# Valeur de retour : le nombre minimal de tests qu'il faut faire
#                   en pire cas pour déterminer le seuil de solidité
#                   d'une fenêtre
# Doit retourner la réponse comme un int.
#
# Function to complete. Do not change its signature.
# N : Maximum force
# k : Number of windows available
# return value : Minimum number of tests needed in the worst case
#               to find the solidity threshold of a window
# Must return the answer as an int.
import sys
import math


"""def vitre(N, k):

    return -1
"""


def whenKIsTwo(N):
    if N == 0:
        return 0
    first = 1
    while ((first*(first+1))/2) < N:
        first += 1
    # print(first)
    return first


def nbTest(x, N, k):

    table = []

    for i in range(0, N+1):
        table.append([])

    # lineValue = x*math.ceil(math.log2(N/x))
    seuilLog = math.log2(N)
    limit = math.ceil(seuilLog)

    for i in range(0, N+1):
        for j in range(0, k+1):
            if i < x or j < x:
                table[i].append(N)
            elif j == 1:
                table[i].append(i-1)
            else:
                table[i].append(limit)

    """print(f" X = {x} for N : {N}, k : {k}")
    print(f" limit : {limit}")
    for i in table:
        print(i)"""

    return table


def vitre(N, k):
    s = []

    for i in range(1, N):
        s.append(nbTest(i, N, k)[N][k])
        # print(f" value {s[i-1]} , x : {i}, N : {N}, k : {k}")
    print(N, k)
    # print(s)
    # print(min(s))
    return min(s)


# Fonction main, vous ne devriez pas avoir à modifier
# Main function, you shouldn't have to modify it


def main(args):
    N = int(args[0])
    k = int(args[1])

    answer = vitre(N, k)
    print(answer)


if __name__ == '__main__':
    main(sys.argv[1:])

# main([8, 6])


# print(whenKIsTwo(3))


def whenKIsThree(N):

    for i in range(-whenKIsTwo(N) + 1, (N-whenKIsTwo(N))-1):
        first = whenKIsTwo(N) + i
        tab = [first]
        while sum(tab) < N:
            tab.append(first + len(tab))
        print(tab)

        sumDesWKis2 = 0

        for i in tab[0:len(tab)-1]:
            sumDesWKis2 += whenKIsTwo(i-1)
        sumDesWKis2 += whenKIsTwo(N - sum(tab[0:len(tab)-1]))

        print(sumDesWKis2)

    """cut = whenKIsTwo(N)

    result = 1 + whenKIsTwo(cut-1)"""

    return


# print(whenKIsThree(25))

"""
def sommeIaN(N):
    return (N*(N+1))/2


def doubleSum(N):
    soluce = 0
    for i in range(1, N):
        soluce += sommeIaN(i)
    return soluce


soluce = 0
for i in range(1, 3):
    soluce += doubleSum(i)
print(soluce)
"""

"""tab = []
for i in range(1, 5):
    tab.append(i)
print(tab)
print(whenKIsTwo(25))
"""

"""main([25, 3])


print(whenKIsTwo(4))"""


"""def whenKisOne(N):
    if N <= 0:
        return 0
    return N-1


n = 25
when = whenKIsTwo(n)

for j in range(when, when+3):
    one = []
    two = []
    print(f" j = {j}")
    for i in range(1, when):
        print(f" avec {i} test apply WhenKis on {when-i+1} ")
        # print(f" ONE : {i+whenKisOne(when-i+1)}")
        one.append(i+whenKisOne(when-i+1))
        # print(f" TWO : {i + min(whenKIsTwo(when-i+1), whenKisOne(when-i+1))}")
        two.append(i + min(whenKIsTwo(when-i+1), whenKisOne(when-i+1)))
    print(f" one : {one}")
    print(f" two : {two}")


for i in range(1, 15):
    print(f" i : {i} ----> {whenKIsTwo(i)}")
"""
