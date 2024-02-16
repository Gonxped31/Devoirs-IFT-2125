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

def write(fileName, content):
    #écrire la sortie dans un fichier/write output in file
    file = open(fileName, "w")
    file.write(content)
    file.close()


#Fonction main/Main function
def main(args):
    input_file = args[0]
    output_file = args[1]
    #TODO : Continuer ici/Complete here...
    #Vous pouvez découper votre code en d'autres fonctions...
    #You may split your code in other functions...



#Kruskal algorithm (for low density)
#graph = ['nodes': [{'id':id, 'x':..., 'y':...},{'id':id, 'x':..., 'y':...}]
#         'edges': [{'source':id, 'destination':id, 'weight':...}]']
def prim_priority_quue(graph):
    nodes = graph['nodes']
    edges = graph['edges']
    minimal_weight = 0
    visited_nodes = {node['id']: False for node in nodes}
    mst = []

    initial_node_index = 0
    visited_nodes[initial_node_index] = True
    initial_node = nodes[initial_node_index]
    priority_queue = PriorityQueue()

    for edge in edges:
        if edge['source'] == initial_node['id']: #or edge['destination'] == initial_node['id']:
            priority_queue.put((edge['weight'], edge))
    
    while priority_queue.qsize() > 0:
        current_edge = priority_queue.get()
        destination = current_edge['destination']

        if visited_nodes[destination]:
            continue

        visited_nodes[destination] = True
        mst.append(current_edge)

        for edge in edges:
            if edge['source'] == destination: #or edge['destination'] == initial_node['id']:
                if not visited_nodes[edge['destination']]:
                    priority_queue.put((edge['weight'], edge))

    for edge in mst:
        minimal_weight += edge['weight']

    return minimal_weight

#Prim algorithm implemented with array (for hight density)
def prim_array():
    pass

#NE PAS TOUCHER
#DO NOT TOUCH
if __name__ == '__main__':
    main(sys.argv[1:])
