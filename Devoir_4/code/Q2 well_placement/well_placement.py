# Gbian Bio Samir, 20250793
# Sourou Johann, 20227958

import sys

def read_problem(input_file="input.txt"):
    with open(input_file, "r") as file:
        lines = file.readlines()
    graph = [list(map(int, line.strip())) for line in lines[1:]]
    return graph

def write(fileName, content):
    with open(fileName, "w") as file:
        file.write(content)

def dfs(graph, start_i, start_j, visited_nodes):
    stack = [(start_i, start_j)]
    count = 0

    while stack:
        i, j = stack.pop()
        if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]):
            continue
        if visited_nodes[i][j] or graph[i][j] != 1:
            continue

        visited_nodes[i][j] = True
        count += 1

        stack.append((i-1, j))
        stack.append((i+1, j))
        stack.append((i, j-1))
        stack.append((i, j+1))

    return count

def main(args):
    input_file = args[0]
    output_file = args[1]
    graph = read_problem(input_file)
    rows, cols = len(graph), len(graph[0])
    visited_nodes = [[False] * cols for _ in range(rows)]
    best_well = 0

    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1 and not visited_nodes[i][j]:
                best_well = max(best_well, dfs(graph, i, j, visited_nodes))

    answer = best_well

    write(output_file, str(answer))


# NE PAS TOUCHER
# DO NOT TOUCH
if __name__ == "__main__":
    main(sys.argv[1:])
