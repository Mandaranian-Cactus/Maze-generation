import random
from collections import deque

class tile:
    def __init__(self):
        self.up = True
        self.down = True
        self.left = True
        self.right = True


w, h = 10,10
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


visual_grid = [[1 for i in range(len(grid[0]) * 2 + 1)] for i in range(len(grid) * 2 + 1)]
dq= deque([[sx, sy]])
print("start", sx, sy, sx * 2 + 1, sy * 2 + 1)
print(*grid, sep = '\n')

while dq:
    for i in range(len(dq)):
        x, y = dq.popleft()
        visual_grid[y * 2 + 1][x * 2 + 1] = 0
        for dir in grid[y][x]:
            if dir == "E":
                visual_grid[y * 2 + 1][x * 2 + 1 + 1] = 0
                dq.append([x + 1, y])
            elif dir == "W":
                visual_grid[y * 2 + 1][x * 2 + 1- 1] = 0
                dq.append([x - 1, y])
            elif dir == "N":
                visual_grid[y * 2 + 1 - 1][x * 2 + 1] = 0
                dq.append([x, y - 1])
            elif dir == "S":
                visual_grid[y * 2 + 1 + 1][x * 2 + 1] = 0
                dq.append([x, y + 1])

print(*visual_grid, sep ='\n', end = '\n\n')
print(visual_grid)
