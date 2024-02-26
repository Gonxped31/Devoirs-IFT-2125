# Nom, Matricule
# Nom, Matricule

import math
import sys


def read_problem(input_file="input.txt"):
    # lecture du fichier/file reading
    file = open(input_file, "r")
    lines = file.readlines()

    # process the file lines for the problem
    ldcn = []
    position = []

    for l in lines[0].split(" "):
        ldcn.append(int(l))
    for i in range(1, len(lines)):
        position.append(int(lines[i]))

    file.close()
    return (ldcn, position)


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]

    ldcn, position = read_problem(input_file)
    l = ldcn[0]
    d = ldcn[1]
    c = ldcn[2]
    n = ldcn[3]

    bridge = []
    for i in range(0, l+1):
        if (i < c or i > l-c):
            bridge.append(0)
        else:
            bridge.append(1)

    for pos in position:
        for i in range(pos-d+1, pos+d):
            bridge[i] = 0

    solution = 0

    for i in range(0, len(bridge)):
        if bridge[i] == 1:
            solution += 1
            for j in range(i-d+1, i+d):
                bridge[j] = 0

    print(solution)
    write(output_file, str(solution))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
