from colorama import init, Fore
import random
from random import shuffle, randrange

class Strategy :
    def __init__(self):
        pass

    def Apply(self):
        print("Applying Abstract Strategy")

    def print_maze(self):
        print("Maze")


class Algorithm1(Strategy) :
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height

    # Randomized Prim's algorithm
    def Apply(self):
        # Initialize the grid, visitation flags, and counts
        vis = [[0] * self.width + [1] for _ in range(self.height)] + [[1] * (self.width + 1)]
        counts = [[0] * self.width for _ in range(self.height)]
        ver = [["|  "] * self.width + ['|'] for _ in range(self.height)] + [[]]
        hor = [["+--"] * self.width + ['+'] for _ in range(self.height + 1)]

        def walk(x, y):
            vis[y][x] = 1
            directions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            counts[y][x] += 1
            for dx, dy in directions:
                if 0 <= dx < self.width and 0 <= dy < self.height:
                    counts[dy][dx] += 1
            
            valid_directions = [(xx, yy) for xx, yy in directions if 0 <= xx < self.width and 0 <= yy < self.height and not vis[yy][xx]]
            valid_directions.sort(key=lambda pos: counts[pos[1]][pos[0]])
            shuffle(valid_directions)

            for (xx, yy) in valid_directions:
                if vis[yy][xx]: continue
                if xx == x: hor[max(y, yy)][x] = "+  "
                if yy == y: ver[y][max(x, xx)] = "   "
                walk(xx, yy)

        walk(randrange(self.width), randrange(self.height))

        # Add an entrance and an exit
        # Entrance at top left, exit at bottom right for maximum path length
        hor[0][0] = "+  "
        hor[self.height][self.width-3] = "+  "
        
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

    def DoSomething(self):
        #super().DoSomething()
        print('Do something')

algo1 = Algorithm1(20, 10)
print(algo1.Apply())