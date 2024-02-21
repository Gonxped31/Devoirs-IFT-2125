import math

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

def composant():
    pass

def fusion():
    pass

def calculate_distance(point_1, point_2):
    return math.sqrt(((point_2['x']-point_1['x'])**2) + ((point_2['y']-point_1['y'])**2))


def kruskal(nodes, edges):
    mst = []
    pass