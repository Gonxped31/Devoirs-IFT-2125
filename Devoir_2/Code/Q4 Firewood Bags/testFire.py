
b6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
      16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
T6 = [34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34,
      34, 34, 34, 34, 34, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 0]
# b6 = b6[::-1]


def calculabeWoodNobUsed(number):
    return T6[b6.index(number)]


# print(calculabeWoodNobUsed(1))
maxWood = 30


def binarySearch(maxWood, x):
    if x > maxWood or x < 1:
        return
    else:
        return binaireRecu(1, maxWood, x)


def binaireRecu(i, j, x):
    if calculabeWoodNobUsed(i) == calculabeWoodNobUsed(j):
        return i
    else:
        k = (i+j)//2
        if x >= calculabeWoodNobUsed(k):
            return binaireRecu(i, k, x)
        else:
            return binaireRecu(k+1, j, x)


print(f"b rechercher : {T6[binarySearch(0)]} ")
print(f"index : {binarySearch(0)}")

print(T6.index(0))
