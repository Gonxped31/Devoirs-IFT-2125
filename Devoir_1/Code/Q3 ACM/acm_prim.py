import math
import time

INFINITY = math.inf

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

#Find the closest node
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

def code(input_file):
    start_parse = time.time()
    lines = read_problems(input_file)
    nodes = convert_nodes(lines)
    end_parse = time.time()

    print(f'parsing time {input_file[-5]}: {round(end_parse - start_parse, 3)} s {round((end_parse - start_parse)/60, 3)} min')

    result = []
    start_time = time.time()
    for node in nodes:
        result.append(prim(create_adjacency_matrix(node)))
    end_time = time.time()

    content = prepare_content(result)
    write(f'output{input_file[-5]}.txt', content)
    print(f'Total time {input_file[-5]}: {round(end_time - start_parse, 3)} s {round((end_time - start_parse)/60, 3)} min \n')

    #print(f'Result for input {input_file[-5]}: {result}')
    #print(f'Execution time: {end_time - start_time}')

for i in range(9):
    code(f'input{i}.txt')


