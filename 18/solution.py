from sys import stdin

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
SIZE = 70

falling_bytes = []
for line in stdin:
    x_str, y_str = line.split(',')
    falling_bytes.append((int(x_str), int(y_str)))

grid = [[False] * (SIZE + 1) for _ in range(SIZE + 1)]

for i in range(1024):
    falling_byte = falling_bytes[i]
    grid[falling_byte[0]][falling_byte[1]] = True

def within_grid(node):
    return node[0] >= 0 and node[1] >= 0 and node[0] <= SIZE and node[1] <= SIZE

def add_vector(a, b):
    return (a[0] + b[0], a[1] + b[1])

def bfs(grid, start, end):
    visited = set()
    search_nodes = [start]
    next_search_nodes = []
    steps = 0

    while len(search_nodes) > 0:
        while len(search_nodes) > 0:
            node = search_nodes.pop(0)

            if node == end:
                return steps

            if not within_grid(node) or grid[node[0]][node[1]]:
                continue

            if node in visited:
                continue
            visited.add(node)

            for dir in DIR:
                next_search_nodes.append(add_vector(node, dir))

        search_nodes = next_search_nodes
        next_search_nodes = []
        steps += 1

    return -1

print(bfs(grid, (0, 0), (SIZE, SIZE)))

for i in range(1024, len(falling_bytes)):
    falling_byte = falling_bytes[i]
    grid[falling_byte[0]][falling_byte[1]] = True

    if (bfs(grid, (0, 0), (SIZE, SIZE)) == -1):
        print(str(falling_byte[0]) + ',' + str(falling_byte[1]))
        break
