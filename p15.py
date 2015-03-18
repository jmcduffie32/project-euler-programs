grid = [[0 for x in range(21)] for x in range(21)]
for x in range(21):
    grid[x][0] = 1
    grid[0][x] = 1

for y in range(1,21):
    for x in range(1,21):
        grid[x][y] = int(grid[x-1][y]+grid[x][y-1])

print grid
