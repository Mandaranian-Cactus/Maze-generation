import random
from collections import deque

class tile:
    def __init__(self):
        self.up = True
        self.down = True
        self.left = True
        self.right = True


w, h = 3, 3
grid = [[[] for i in range(w)] for i in range(h)]


# Recursive backtracking
def dfs(grid, x, y):

    dx = {"N":0,"E":1,"S":0,"W":-1}
    dy = {"N":-1,"E":0,"S":1,"W":0}
    dirs = ["N","E","S","W"]
    random.shuffle(dirs)
    flag = False
    for dir in dirs:

        # New x and new y
        cx = x + dx[dir]
        cy = y + dy[dir]

        if cy in range(len(grid)) and cx in range(len(grid[0])) and grid[cy][cx] == []:
            grid[y][x].append(dir)
            dfs(grid, cx, cy)
            flag = True

    if not flag:
        grid[y][x].append("X")


sx, sy = random.randrange(len(grid[0])), random.randrange(len(grid))
dfs(grid, sx, sy)


visual_grid = [[tile() for i in range(len(grid[0]))] for i in range(len(grid))]
dq= deque([[sx, sy]])
print(*grid, sep = '\n')

while len(dq) > 0:
    for i in range(len(dq)):
        x, y = dq.popleft()
        for dir in grid[y][x]:
            if dir == "N":
                visual_grid[y][x].up = False
                visual_grid[y - 1][x].down = False
                dq.append([x, y - 1])
            elif dir == "S":
                visual_grid[y][x].down = False
                visual_grid[y + 1][x].up = False
                dq.append([x, y + 1])
            elif dir == "E":
                visual_grid[y][x].right = False
                visual_grid[y][x + 1].left = False
                dq.append([x + 1, y])
            elif dir == "W":
                visual_grid[y][x].left = False
                visual_grid[y][x - 1].right = False
                dq.append([x - 1, y])

# Begin display
for row in visual_grid:
    for sqr in row:
        print("|", end = '')
        if sqr.up: print("=", end = '')
        else: print(" ", end = '')
        print("|", end ='')
    print()
    for sqr in row:
        if sqr.left: print("|", end = '')
        else: print(" ", end = '')
        print(" ", end = '')
        if sqr.right: print("|", end ='')
        else: print(" ", end ='')
    print()
    for sqr in row:
        print("|", end='')
        if sqr.down:
            print("=", end='')
        else:
            print(" ", end='')
        print("|", end ='')
    print()