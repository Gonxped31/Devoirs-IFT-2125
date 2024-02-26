import numpy as np


def f1(x):
    if x == 0:
        return 0
    if x == 1:
        return 2
    else:
        return 9*f1(x/2) + 8*((x/2)**2)


print(f1(8))


# Définir la matrice A
A = np.array([[1, 1, 0, 0],
              [9, 1, 1, 1],
              [81, 1, 2, 4],
              [729, 1, 3, 9]])

# Définir le vecteur b
b = np.array([2, 26, 266, 2522])

# Résoudre le système d'équations linéaires A * x = b
x = np.linalg.solve(A, b)

# Afficher la solution
print(f" Solution {x}")
