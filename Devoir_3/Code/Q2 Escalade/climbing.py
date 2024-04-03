

no = 1
fichier = "wall" + str(no) + ".txt"

with open(fichier) as file:
    lines = file.readlines()

matrice = []

for line in lines:
    row = []
    for i in line.split(","):
        row.append(int(i))
    matrice.append(row)


for i in matrice:
    print(i)


# m * n
m = len(matrice)
n = len(matrice[0])

print(m, n)
