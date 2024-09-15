"""
Given:
A 2d grid of m x n
Each cell has 2 possible values: 0 = can walk, -1 = obstacle
Start and end coordinates (x, y) (x, y)
 

Find the shortest path from start to end.
 

Constraints:
0 < m <= n < 10000
 

Possible output:
Min distance
1 if not possible to find a path from start to end
"""

# m x n
# 0 or 1, walk or cant
# start and end coord x, y

from collections import deque

def travel(grid, start, end):
    table = [[-1 for index in range(len(grid[0]))] for index in range(len(grid))] # traversal table to -1

    queue = deque()
    queue.append(start)

    # initialize table values
    table[start[0]][start[1]] = 0 # initial distance of 0

    while(queue):
        current = queue.popleft()
        x = current[0]
        y = current[1]

        # check left right up down
        if (x-1 >= 0 and grid[x-1][y] == 0): # check left
            if (table[x-1][y] == -1 or table[x-1][y] > table[x][y] + 1):
                table[x-1][y] = table[x][y] + 1
                queue.append((x-1, y))
        if (x+1 < len(grid) and grid[x+1][y] == 0): # check right
            if (table[x+1][y] == -1 or table[x+1][y] > table[x][y] + 1):
                table[x+1][y] = table[x][y] + 1
                queue.append((x+1, y))

        if (y+1 < len(grid[0]) and grid[x][y+1] == 0): # check up
            if (table[x][y+1] == -1 or table[x][y+1] > table[x][y] + 1):
                table[x][y+1] = table[x][y] + 1
                queue.append((x, y+1))
        if (y-1 >= 0 and grid[x][y-1] == 0): # check down
            if (table[x][y-1] == -1 or table[x][y-1] > table[x][y] + 1):
                table[x][y-1] = table[x][y] + 1
                queue.append((x, y-1))

    return table[end[0]][end[1]]

grid = [[0, -1, 0, 0],[0, 0, 0, -1],[0, -1, -1, -1],[0, 0, 0, 0]]
grid_2 = [[0, -1, 0, 0],[-1, 0, -1, -1],[0, -1, -1, -1],[0, -1, -1, -1]]
start = (0, 3)
end = (3, 0)

# [
# [0, -1, 0, 0],
# [0, 0, 0, -1],
# [0, -1, -1, -1],
# [0, 0, 0, 0]
# ]

# [
# [0, -1, 0, 0],
# [-1, 0, -1, -1],
# [0, -1, -1, -1],
# [0, -1, -1, -1]
# ]

print(travel(grid_2, start, end))