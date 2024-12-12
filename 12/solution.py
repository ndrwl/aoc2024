from sys import stdin
from collections import defaultdict

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
MERGE_BORDERS = True

map = []

for line in stdin:
    map.append(list(line.strip()))

def within_map(map, x, y):
    return x >= 0 and y >= 0 and x < len(map) and y < len(map[0])

def get_map(map, x, y):
    if not within_map(map, x, y):
        return ''
    return map[x][y]

def count_borders(visited):
    min_x = min(x for (x, _) in visited)
    max_x = max(x for (x, _) in visited)
    min_y = min(y for (_, y) in visited)
    max_y = max(y for (_, y) in visited)

    border_count = 0

    # X borders
    for x in range(min_x - 1, max_x + 2):
        current_edge = (False, False)
        for y in range(min_y, max_y + 1):
            edge = ((x, y) in visited, (x + 1, y) in visited)
            is_edge = edge[0] != edge[1]

            if not MERGE_BORDERS:
                border_count += is_edge
                continue

            if current_edge != edge and is_edge:
                border_count += 1
            current_edge = edge

    # Y borders
    for y in range(min_y - 1, max_y + 2):
        current_edge = (False, False)
        for x in range(min_x, max_x + 1):
            edge = ((x, y) in visited, (x, y + 1) in visited)
            is_edge = edge[0] != edge[1]

            if not MERGE_BORDERS:
                border_count += is_edge
                continue

            if current_edge != edge and is_edge:
                border_count += 1
            current_edge = edge

    return border_count

def calculate_cost(map, init_x, init_y):
    crop_type = get_map(map, init_x, init_y)

    visited = set()
    visit_queue = []

    visited.add((init_x, init_y))
    visit_queue.append((init_x, init_y))

    while len(visit_queue) > 0:
        (x, y) = visit_queue.pop(0)

        for (dir_x, dir_y) in DIR:
            new_x, new_y = x + dir_x, y + dir_y
            if (new_x, new_y) in visited:
                continue
            if get_map(map, new_x, new_y) == crop_type:
                visited.add((new_x, new_y))
                visit_queue.append((new_x, new_y))

    for (x, y) in visited:
        map[x][y] = ''

    return count_borders(visited) * len(visited)

cost = 0

for x in range(len(map)):
    for y in range(len(map[0])):
        if get_map(map, x, y) != '':
            cost += calculate_cost(map, x, y)

print(cost)
