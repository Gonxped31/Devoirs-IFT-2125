from collections import deque
import random


class Maze:
    def __init__(self, n, m) -> None:
        self.n = n
        self.m = m
        Cells = []
        k = (n+1)*m
        for i in range(1, n*m + 1):
            j = (i-1)//m
            Cells.append(Cell(i, i+m, i+k+j, i+k+1+j))
        self.AllCells = Cells

    def getCell(self, i):
        if (i < 0 or i >= self.n*self.m):
            return self.AllCells[0]
        else:
            return self.AllCells[i]

    def getSize(self):
        return self.n, self.m

    def modVisitStatus(self, i, newValue):
        (self.AllCells[i]).modVisitStatus(newValue)
        return

    def isVisited(self, i):
        return (self.AllCells[i]).isVisited()

    def neighborsOf(self, i):
        n = self.n
        m = self.m
        neighbors = []
        if (i < 0 or i >= self.n*self.m):
            return self.AllCells[0]
        else:
            if (i == 0):
                neighbors = [1, m]
            elif (i == m-1):
                neighbors = [i-1, i+m]
            elif (i == m*(n-1)):
                neighbors = [i-m, i+1]
            elif (i == m*n-1):
                neighbors = [i-1, i-m]
            elif (i % m != 0 and i % m != m-1 and i//m != 0 and i//m != n-1):
                neighbors = [i+1, i-1, i+m, i-m]
            elif (i % m == 0):
                neighbors = [i+1, i+m, i-m]
            elif (i % m == m-1):
                neighbors = [i-1, i+m, i-m]
            elif (i // m == 0):
                neighbors = [i+1, i-1, i+m]
            elif (i // m == n-1):
                neighbors = [i+1, i-1, i-m]
        return neighbors

    def neighborsNotVisited(self, i):
        result = []
        neighbors = self.neighborsOf(i)
        for j in range(0, len(neighbors)):
            if (self.AllCells[neighbors[j]].isVisited()):
                continue
            result.append(neighbors[j])
        return result

    def removeWall(self, i, j):
        communeWall = (self.AllCells[i]).communeWall(self.AllCells[j])
        if len(communeWall) != 0:
            (self.AllCells[i]).replaceWall(communeWall[0],
                                           2*(self.n)*(self.m) + (self.n) + (self.m) + 1)
            (self.AllCells[j]).replaceWall(communeWall[0],
                                           2*(self.n)*(self.m) + (self.n) + (self.m) + 1)
        else:
            print("Error in removeWall")
        return


class Cell:
    def __init__(self, n1, n2, n3, n4) -> None:
        self.wall = [n1, n2, n3, n4]
        self.visited = False

    def isVisited(self):
        return self.visited

    def modVisitStatus(self, newValue):
        self.visited = newValue
        return

    def communeWall(self, cell1):
        wall1 = cell1.getWall()
        selfWall = self.wall
        communeWall = []
        for i in wall1:
            for j in selfWall:
                if i == j:
                    communeWall.append(i)
        return communeWall

    def getWall(self):
        return self.wall

    def contain(self, n):
        return n in self.getWall()

    def replaceWall(self, wall, newWall):
        self.wall.remove(wall)
        self.wall.append(newWall)


AllCells = []
cell1 = Cell(1, 2, 3, 4)
cell2 = Cell(4, 2, 6, 7)

# print(cell1.communeWall(cell2))


def deepFistSearchIterative(maze):
    n, m = maze.getSize()
    stack = deque()
    visited = []
    stack.append(random.randint(0, n*m-1))

    while len(stack) != 0:
        index = stack.pop()
        visited.append(index)
        currentNeighbors = maze.neighborsOf(index)
        random.shuffle(currentNeighbors)
        for neigh in currentNeighbors:
            if neigh not in visited:
                stack.append(index)
                maze.removeWall(index, neigh)
                stack.append(neigh)
                visited.append(neigh)
                break
    return maze


def createMaze(n, m):
    maze = Maze(n, m)
    maze = deepFistSearchIterative(maze)
    return maze


def getMazeEdges(maze):
    n, m = maze.getSize()
    mazeEdge = []
    for i in range(0, n*m):
        wall = maze.getCell(i).getWall()
        for j in wall:
            mazeEdge.append(j)
    mazeEdge = (set(mazeEdge)).difference(
        {2*(n)*(m)+n+m + 1, m*(n+1) + 1, 2*(n)*(m)+n+m})
    return list(mazeEdge)


def write(fileName, content):
    with open(fileName, "w") as file:
        file.write(content)


cell_size = 10  # mm
wall_height = 10  # mm
wall_thickness = 1  # mm


def drawingMaze(maze):
    title = f"// Labyrinth generated for openscad \n// IFT2125 - H24 \n// Authors : Bio Samir Gbian, Johann Sourou"
    base = """
    difference(){
    union(){
    // base plate
    translate([0,0,0]){
    cube([100,100,1], center=false);}
    """
    bigString = title + base + "\n"

    n, m = maze.getSize()
    mazeEdges = getMazeEdges(maze)
    for k in range(0, len(mazeEdges)):
        i = mazeEdges[k]
        if i < m*(n+1) + 1:
            y = 100 - ((i-1)//m)*(100/n)
            x = (100/m)*((i-1) % m)
            z = 0
            str = f" translate({[x, y, z]}){{cube([10,1,10], center=false);}}"
            bigString += str + "\n"
        else:
            l = i-m*(n+1) + m + 1
            y = 100 - ((l-1)//(m+1))*(100/n)
            x = (100/m)*((l-1) % (m+1))
            z = 0
            str = f" translate({[x, y, z]})" + \
                f"{{rotate([0,0,90]){{cube([11,1,10], center=false);}}}}"
            bigString += str + "\n"
    bigString += """
    // logo
    translate([1,-0.2,1]){
    rotate([90,0,0]){
    linear_extrude(1) text( "IFT2125 RM", size= 7.0);
    }
    }
    } }
    """
    return bigString


# mazeInString = drawingMaze(createMaze(10, 10))
# write("maze.txt", mazeInString)
# print(mazeInString)


title = f"// Labyrinth generated for openscad \n// IFT2125 - H24 \n// Authors : Bio Samir Gbian, Johann Sourou"
base = """
    difference(){
    union(){
    // base plate
    translate([0,0,0]){
    cube([100,100,1], center=false);}
    """
bigString = title + base + "\n"

maze = createMaze(10, 10)
n, m = maze.getSize()
mazeEdges = getMazeEdges(maze)
print(mazeEdges)

if (cell_size*max(n, m) > 120):
    cell_size = 120//max(n, m) + 1

# cell_size = (max(n, m))//20

for k in range(0, len(mazeEdges)):
    i = mazeEdges[k]
    if i <= m*(n+1):
        y = cell_size*(n - (i-1)//m)
        x = cell_size*((i-1) % m)
        z = 0
        """str = f" translate({[x, y, z]}){{cube([{cell_size},{
            wall_thickness},{wall_height}], center=false);}}"
        bigString += str + "\n" """
    else:
        l = i-m*(n+1)
        y = cell_size*(n - ((l-1)//(m+1)))
        x = cell_size*((l-1) % (m+1))
        z = 0
        str = f" translate({[x, y, z]})" + \
            f"{{rotate([0,0,90]){{cube([{cell_size+1},{wall_thickness},{wall_height}], center=false);}}}}"
        bigString += str + "\n"
bigString += """
    // logo
    translate([1,-0.2,1]){
    rotate([90,0,0]){
    linear_extrude(1) text( "IFT2125 RM", size= 7.0);
    }
    }
    } }
    """

# Cell.
write("maze.txt", bigString)
