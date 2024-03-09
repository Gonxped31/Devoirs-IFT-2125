# Nom, Matricule
# Nom, Matricule

import math
import sys

def read_problem(input_file="input.txt"):
    return list(map(lambda x: tuple(map(lambda y: int(y), x)), 
                    list(map(lambda x: x.split(' '), 
                             list(map( lambda x: x.replace('\n', ''), 
                                      open(input_file, 'r').readlines()))))))


def write(fileName, content):
    """Écrire la sortie dans un fichier/write output in file"""
    file = open(fileName, "w")
    file.write(content)
    file.close()


def main(args):
    """Fonction main/Main function"""
    input_file = args[0]
    output_file = args[1]
    inputs = read_problem(input_file)
    J = int(inputs[0][0])
    W = list(map(lambda x: int(x) , inputs[1]))
    min_bound = math.floor(sum(W) / J)
    max_bound = math.ceil(1.4*(min_bound + math.ceil(math.log(max(W)))))
    intervall = list(range(min_bound, max_bound + 1))
    print(intervall)

    for B in intervall:
        if J >= 100:
            j = 1
        else:
            j = 0
        nb_woods = 0
        for w in W:
            j += math.ceil(w/B)
            nb_woods += w
            
        if j == J and nb_woods == sum(W):
            write(output_file, str(B))
            break

# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    #main(sys.argv[1:])
    main(['C:\\Users\\Samir\\Documents\\GitHub\\Devoirs-IFT-2125\\Devoir_2\\Code\\Q4 Firewood Bags\\input9.txt', 'output9.txt'])
