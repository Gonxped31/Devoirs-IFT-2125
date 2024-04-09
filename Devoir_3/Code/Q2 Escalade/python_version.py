def parse(input_file):
    file = open(input_file, 'r')
    lines = file.readlines()
    inputs = list(map(lambda x: x.replace('\n', '').split(','), lines))
    return list(map(lambda x: [eval(i) for i in x], inputs))

def algo(file):
    data = parse(file)
    lines, columns = len(data), len(data[0])
    dist_tab = [data[-1]] + [[0] * columns for _ in range(lines - 1)]

    for i in range(1, lines):
        for j in range(columns):
            actual_line = lines - 1 - i

            minValue = dist_tab[i - 1][j] + data[actual_line][j]

            if j > 0:
                left = dist_tab[i][j - 1] + data[actual_line][j]
                minValue = min(minValue, left)

            right_sum = 0
            for k in range(j + 1, columns):
                right_sum += data[actual_line][k]
                dist = dist_tab[i - 1][k] + right_sum + data[actual_line][j]
                minValue = min(minValue, dist)

            dist_tab[i][j] = minValue

    return min(dist_tab[-1])

print(algo('Devoir_3\Code\Q2 Escalade\wall1.txt'))
print(algo('Devoir_3\Code\Q2 Escalade\wall2.txt'))
print(algo('Devoir_3\Code\Q2 Escalade\wall3.txt'))
print(algo('Devoir_3\Code\Q2 Escalade\wall4.txt'))
print(algo('Devoir_3\Code\Q2 Escalade\wall5.txt'))
print(algo('Devoir_3\Code\Q2 Escalade\wall6.txt'))