#Nom, Matricule
#Nom, Matricule
from queue import PriorityQueue
import math
import sys
INFINITY = math.inf

#Fonctions pour lire/écrire dans les fichier. Vous pouvez les modifier, 
#faire du parsing, rajouter une valeur de retour, mais n'utilisez pas
#d'autres librairies.
#Functions to read/write in files. you can modify them, do some parsing,
#add a return value, but don't use other librairies
def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines()
    file.close()
    return lines

def prepare_content(result):
    content = ''
    for elem in result:
        content += f'{round(elem, 3)}\n'
    return content

def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()

def convert_nodes(lines):
    new_lines = list(map(lambda x: x.strip().replace('\n', ''), lines))[2::]
    new_lines.append('0')
    problems = []
    tmp = []
    #print(new_lines)
    for i in range(len(new_lines)):
        if len(new_lines[i]) > 1:
            tmp.append(new_lines[i])
        else:
            problems.append(tmp)
            tmp = []
    
    #print(problems)
    #print(len(problems))
    nodes = []
    for problem in problems:
        arr = []
        for i in range(len(problem)):
            #print(problem)
            splitted_node = problem[i].split(' ')
            x,y = splitted_node[0], splitted_node[1]
            arr.append( {'id': i, 'x': float(x), 'y': float(y)} )
        nodes.append(arr)
    #print(nodes)
    return nodes

def min_key(keys, mst, num_of_nodes):
    min = INFINITY

    for i in range(num_of_nodes):
        if keys[i] < min and mst[i] == False:
            min = keys[i]
            min_index = i

    return min_index

def prim(matrix):
    #print_mat(matrix)
    num_of_nodes = len(matrix[0])
    keys = [INFINITY]*num_of_nodes
    parent = [None]*num_of_nodes
    mst = [False]*num_of_nodes
    keys[0] = 0
    parent[0] = -1

    min_weight = 0

    for _ in range(num_of_nodes):
        #Find the closest node and mark it as visited
        closest_node = min_key(keys, mst, num_of_nodes)
        #print("Keys", keys)
        mst[closest_node] = True
        #print("Closest node", closest_node)
        #update the only if the distance is smaller
        for j in range(num_of_nodes):
            if matrix[closest_node][j] > 0 and mst[j] == False and keys[j] > matrix[closest_node][j]:
                keys[j] = matrix[closest_node][j]
                parent[j] = closest_node

    for i in range(num_of_nodes):
        min_weight += keys[i]
    return min_weight

def calculate_distance(point_1, point_2):
    return math.sqrt(((point_2['x']-point_1['x'])**2) + ((point_2['y']-point_1['y'])**2))

def create_adjacency_matrix(nodes):
    mat = []
    for i in range(len(nodes)):
        line = []
        for j in range(len(nodes)):
            #print(nodes[i], nodes[j])
            dist = calculate_distance(nodes[i], nodes[j])
            line.append(dist)
        mat.append(line)
    
    return mat

#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    #TODO : Continuer ici/Complete here...
    #Vous pouvez découper votre code en d'autres fonctions...
    #You may split your code in other functions...
    lines = read_problems(input_file)
    nodes = convert_nodes(lines)
    result = []
    for node in nodes:
        result.append(prim(create_adjacency_matrix(node)))

    content = prepare_content(result)
    write(f'output{input_file[-5]}.txt', content)

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
