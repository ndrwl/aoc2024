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
        grid_line = []
        for c in line:
            if c == '#':
                grid_line.append('#')
                grid_line.append('#')
            if c == 'O':
                grid_line.append('[')
                grid_line.append(']')
            if c == '.':
                grid_line.append('.')
                grid_line.append('.')
            if c == '@':
                grid_line.append('@')
                grid_line.append('.')
        grid.append(grid_line)
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

def collect_moveables(grid, dir, start):
    moveables = []

    visited = set()
    visit_queue = []
    next_visit_queue = []
    visit_queue.append(start)

    while len(visit_queue) > 0 or len(next_visit_queue) > 0:
        if len(visit_queue) == 0:
            visit_queue = next_visit_queue
            next_visit_queue = []
        visitor = visit_queue.pop()

        if visitor in visited:
            continue
        visited.add(visitor)

        cell = grid[visitor[0]][visitor[1]]

        if cell == '#':
            return []

        if cell == '.':
            continue

        moveables.append(visitor)
        next_visit_queue.append(add_vector(visitor, dir))

        if cell == '[' and dir[0] != 0:
            visit_queue.append(add_vector(visitor, (0, 1)))

        if cell == ']' and dir[0] != 0:
            visit_queue.append(add_vector(visitor, (0, -1)))

    moveables.reverse()
    return moveables

def move(grid, dir, moveables):
    for start in moveables:
        end = add_vector(start, dir)

        grid[end[0]][end[1]] = grid[start[0]][start[1]]
        grid[start[0]][start[1]] = '.'

def step(grid, dir, player):
    moveables = collect_moveables(grid, dir, player)
    if len(moveables) == 0:
        return player
    move(grid, dir, moveables)
    return add_vector(player, dir)

player = find_player(grid)

for move_str in moves:
    dir = DIR[move_str]
    player = step(grid, dir, player)

sum = 0

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] == '[':
            sum += 100 * x + y

print(sum)
