from queue import PriorityQueue
import math
import sys
import time

def read_problems(input_file):
    # lecture du fichier/file reading
    file = open(input_file,"r")
    lines = file.readlines()
    file.close()
    return lines

def prepare_content(result):
    content = ''
    for elem in result:
        content += f'{round(elem[0], 3)}\n'
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

def prim(nodes, edges):
    graph = {node['id']: [] for node in nodes}
    for edge in edges:
        graph[edge['source']].append((edge['destination'], edge['weight']))
        graph[edge['destination']].append((edge['source'], edge['weight']))
    
    minimal_weight = 0
    visited_nodes = set()
    mst_edges = []

    priority_queue = PriorityQueue()
    initial_node_id = nodes[0]['id']
    visited_nodes.add(initial_node_id)

    for i in range(len(edges)):
        initial_node_id = nodes[i]['id']
        for destination, weight in graph[initial_node_id]:
            priority_queue.put((weight, initial_node_id, destination))



    while not priority_queue.empty():
        weight, source, destination = priority_queue.get()

        if destination in visited_nodes:
            continue
        
        mst_edges.append((source, destination, weight))
        minimal_weight += weight
        visited_nodes.add(destination)

        for next_destination, next_weight in graph[destination]:
            if next_destination not in visited_nodes:
                priority_queue.put((next_weight, destination, next_destination))

    return minimal_weight, mst_edges

def calculate_distance(point_1, point_2):
    return math.sqrt(((point_2['x']-point_1['x'])**2) + ((point_2['y']-point_1['y'])**2))

def create_edges(nodes):

    k = 0
    edges = []
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            edges.append(
                {'source': nodes[i]['id'], 'destination': nodes[j]['id'], 'weight': calculate_distance(nodes[i], nodes[j])}
            )
            k += 1
            edges.append(
                {'source': nodes[j]['id'], 'destination': nodes[i]['id'], 'weight': calculate_distance(nodes[i], nodes[j])}
            )
            k += 1
    return edges

def code(input_file):
    start_parse = time.time()
    lines = read_problems(input_file)
    nodes = convert_nodes(lines)
    edges = []
    for prob in nodes:
        edges.append(create_edges(prob))

    end_parse = time.time()

    #print(f'There is {len(nodes)} nodes and {len(edges)} edges.')

    #print(f'parsing time: {end_parse - start_parse}')
    result = []
    start_time = time.time()
    for node, edge in zip(nodes, edges):
        result.append(prim(node, edge))
    
    end_time = time.time()

    content = prepare_content(result)
    write(f'./Code/Q3 ACM/output{input_file[-5]}.txt', content)
    #print(f'Result for input {input_file[-5]}: {round(result[0][0], 3)}')
    #print(f'Execution time: {end_time - start_time}')

code('./Code/Q3 ACM/input0.txt')