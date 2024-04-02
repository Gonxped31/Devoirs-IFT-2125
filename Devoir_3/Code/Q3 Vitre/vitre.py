#Gbian Bio Samir, 20250793
#Sourou Johann, 20227958

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
import sys


def vitre(N, k):

    T = [[float('inf')] * (N + 1) for _ in range(k + 1)]

    if N == 1:
        return 0

    for i in range(1, k + 1):
        T[i][0] = 0
    
    for j in range(1, N + 1):
        T[1][j] = j

    for i in range(2, k + 1):
        for j in range(1, N + 1):
            for x in range(0, j):
                T[i][j] = min(T[i][j], max(T[i - 1][x], T[i][j - x - 1]) + 1)

    return T[k][N-1]


#Fonction main, vous ne devriez pas avoir à modifier
#Main function, you shouldn't have to modify it
def main(args):
    N = int(args[0])
    k = int(args[1])
    
    answer = vitre(N,k)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])