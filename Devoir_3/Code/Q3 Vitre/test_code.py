#Nom, matricule
#Nom, matricule

#Fonction à compléter. Ne modifiez pas sa signature.
#N : Force maximale
#k : Nombre de fenêtres disponibles
#Valeur de retour : le nombre minimal de tests qu'il faut faire 
#                   en pire cas pour déterminer le seuil de solidité 
#                   d'une fenêtre
#Doit retourner la réponse comme un int.
#
#Function to complete. Do not change its signature.
#N : Maximum force
#k : Number of windows available
#return value : Minimum number of tests needed in the worst case
#               to find the solidity threshold of a window
#Must return the answer as an int. 
from itertools import count
import sys


def bestStrat(N, low, high):
    if (low == high):
        return ()
    i = low + (0 if (N == 1) else bestIndex(N, high - low))
    return (i, bestStrat(N-1, low, i), bestStrat(N, i+1, high))

def choices(N, low, high, strat, breakF):
    if (low == high):
        return ()
    i, S1, S2 = strat
    if (i < breakF):
        return (i, choices(N, 1+i, high, S2, breakF))
    return (i, choices(N-1, low, i, S1, breakF))

def vitre(Fmax, N):
    # L'intervalle des forces à tester est [1, Fmax[
    #  excluant Fmax car on sait déjà qu'elle brise la fenêtre.
    S = bestStrat(N, 1, Fmax)
    return max(count(choices(N, 1, Fmax, S, B)) for B in range(1, Fmax+1))

def bestIndex(n, f):
    pick = f - 1
    for partial in sequence(n):
        if (pick < partial):
            return pick
        pick -= partial

def sequence(N):
    yield 1
    m = 1
    while True:
        yield sum(binomial(m, j) for j in range(0, N))
        m += 1

def factorial(N):
    f = 1
    for i in range(N):
        f *= i+1
    return f

def binomial(N, K):
    return factorial(N) // factorial(K) // factorial(N-K)

#Fonction main, vous ne devriez pas avoir à modifier
#Main function, you shouldn't have to modify it
def main(args):
    N = int(args[0])
    k = int(args[1])
    
    answer = vitre(N,k)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])