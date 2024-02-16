import math
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

def kruskal(nodes, edges):
    mst = []
    sorted_edges = sort_edges(edges)
    print("edges",sorted_edges)
    weights = list(sorted_edges.keys())
    nodes_id = list(map(lambda x: x['id'], nodes))
    print("1->", nodes_id)
    while(len(mst) < (len(nodes) - 1)):
        print("weights",weights)
        min_weight = weights[0]
        min_edges_list = edges[min_weight]
        print(min_edges_list)
        if len(min_edges_list) != 0:
            min_edge = min_edges_list.pop(0)
            print("min edge ",min_edge)
            edges[min_weight] = min_edges_list
            print("2->", nodes_id[min_edge[0]], nodes_id[min_edge[1]])
            if nodes_id[min_edge[0]] != nodes_id[min_edge[1]]:
                mst.append(min_weight)
                if nodes_id[min_edge[0]] > nodes_id[min_edge[1]]:
                    nodes_id[nodes_id[min_edge[0]]] = nodes_id[min_edge[1]]
                else:
                    nodes_id[nodes_id[min_edge[1]]] = nodes_id[min_edge[0]]
        else:
            print("minus")
            weights.pop(0)

    print("MST", mst)
    return sum(mst)

def composant():
    pass

def fusion():
    pass

def calculate_distance(point_1, point_2):
    return math.sqrt(((point_2['x']-point_1['x'])**2) + ((point_2['y']-point_1['y'])**2))

def create_edges(nodes):
    edges = {}
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            source = nodes[i]
            destination = nodes[j]
            weight = calculate_distance(source, destination)
            if weight not in edges:
                edges[weight] = [(source['id'], destination['id'])] 
            else:
                edges[weight].append((source['id'], destination['id']))
    return edges

def sort_edges(edges):
    keys = list(edges.keys())
    keys.sort()
    return {key: edges[key] for key in keys}

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
        result.append(kruskal(node, edge))
    
    end_time = time.time()

    #content = prepare_content(result)
    #write(f'./Code/Q3 ACM/output{input_file[-5]}.txt', content)
    print(result)
    #print(f'Result for input {input_file[-5]}: {round(result[0][0], 3)}')
    #print(f'Execution time: {end_time - start_time}')

code('input1.txt')