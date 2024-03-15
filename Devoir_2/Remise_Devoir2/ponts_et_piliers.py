# Gbian Bio Samir 20250793
# Sourou Johann 20227958

import math
import sys


def read_problem(input_file="input.txt"):
    return list(map(lambda x: tuple(map(lambda y: int(y), x)),
                    list(map(lambda x: x.split(' '),
                             list(map(lambda x: x.replace('\n', ''),
                                      open(input_file, 'r').readlines()))))))


def write(fileName, content):
    file = open(fileName, "w")
    file.write(content)
    file.close()

# Main function


def main(args):
    input_file = args[0]
    output_file = args[1]

    inputs = read_problem(input_file)
    p = inputs.pop(0)
    l, d, c, n = p[0], p[1], p[2], p[3]

    # calcul the number of pillars to build
    if 2*c < l:
        write(output_file, "0")
    elif n == 0:
        write(output_file, str(math.floor((l-2*c)/d) + 1))
    else:
        positions = tuple(sorted(tuple(map(lambda x: x[0], inputs))))
        count, i, j = 0, positions[0], positions[-1]

        count += math.floor((i-c)/d) + math.floor((l-c-j)/d)

        for k in range(len(positions)-1):
            dist = positions[k+1] - positions[k]
            if dist > d:
                count += math.floor(dist/d) - 1

        write(output_file, str(count))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
