import sys

# Gbian Bio Samir 20250793
# Sourou Johann 20227958


def read_problem(input_file="input.txt"):

    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()

    # process the file lines for the problem
    nbDay = int(lines[0])
    fireWoodBags = []
    for i in lines[1].split(" "):
        fireWoodBags.append(int(i))

    file.close()
    return (nbDay, fireWoodBags)


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()

# Calculate the number of day when we take a given b
# The order of this function is O(S), because we iterate on the number of bag


def frequencyOfWoodPerDay(fireWoodBags, bTest):
    rapport = []
    for wood in fireWoodBags:
        if (wood % bTest == 0):
            rapport.append(round(wood/bTest))
        else:
            rapport.append(round(wood/bTest + 0.5))
    return sum(rapport)

# Do a binary search to find the value of the first b with the frequenceOfWoodPerDay is equal to the number of Day given
# The binary search is carried out in log(Max(W)) (because the possible value of b are between 1 and max(W))
# for each recurrsion we use 1 or 2 time frequencyOfWoodPerDay ( O(s) )
# The order of this function is therefore O( s*log(Max(W)))


def binarySearch(fireWoodBags, x):
    return binaireRecu(fireWoodBags, 1, max(fireWoodBags), x)


def binaireRecu(fireWoodBags, i, j, x):
    if frequencyOfWoodPerDay(fireWoodBags, i) == frequencyOfWoodPerDay(fireWoodBags, j):
        return i
    else:
        k = (i+j)//2
        if x >= frequencyOfWoodPerDay(fireWoodBags, k):
            return binaireRecu(fireWoodBags, i, k, x)
        else:
            return binaireRecu(fireWoodBags, k+1, j, x)


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    nbDay, fireWoodBags = read_problem(input_file)
    write(output_file, str(binarySearch(fireWoodBags, nbDay)))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
