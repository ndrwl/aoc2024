from sys import stdin

DIR = {'v' : (1, 0), '^' : (-1, 0), '>' : (0, 1), '<': (0, -1)}

grid = []
moves = []
grid_loaded = False

for line in stdin:
    line = line.strip()
    if len(line) == 0:
        grid_loaded = True
        continue

    if not grid_loaded:
        grid.append(list(line))
    else:
        moves.extend(list(line))

def find_player(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '@':
                return (x, y)
    return (0, 0)

def add_vector(a, b):
    return (a[0] + b[0], a[1] + b[1])

def move(grid, dir, start):
    end = add_vector(start, dir)
    start_cell = grid[start[0]][start[1]]
    end_cell = grid[end[0]][end[1]]

    if end_cell == '#':
        return False

    if end_cell == '.' or move(grid, dir, end):
        grid[start[0]][start[1]] = '.'
        grid[end[0]][end[1]] = start_cell
        return True

    return False

player = find_player(grid)

for move_str in moves:
    dir = DIR[move_str]
    if move(grid, dir, player):
        player = add_vector(player, dir)

sum = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == 'O':
            sum += 100 * x + y

print(sum)
