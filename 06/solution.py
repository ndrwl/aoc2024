from sys import stdin

OBSTACLE = '#'

map = []

for line in stdin:
    map.append(line)

def find_starting_position(map):
    for x in range(len(map)):
        if '^' not in map[x]:
            continue

        y = map[x].find('^')
        return (x, y), (-1, 0)

        # Other cases such as > v < not needed

    return (-1, -1), (0 , 0)

def within_map(map, x, y):
    return x >= 0 and y >= 0 and x < len(map) and y < len(map[0])

def rotate(dir):
    return dir[1], dir[0] * -1

def is_obstacle(map, x, y):
    global OBSTACLE
    return within_map(map, x, y) and map[x][y] == OBSTACLE

def step(pos, dir, map, obstacle):
    next = (pos[0] + dir[0], pos[1] + dir[1])
    if is_obstacle(map, next[0], next[1]) or next == obstacle:
        return pos, rotate(dir)
    return next, dir

def is_loop(starting_pos, starting_dir, map, obstacle):
    visited = set()
    pos = starting_pos
    dir = starting_dir

    while within_map(map, pos[0], pos[1]):
        if (pos, dir) in visited:
            return True
        visited.add((pos, dir))

        pos, dir = step(pos, dir, map, obstacle)
    return False

starting_pos, starting_dir = find_starting_position(map)

visited = set()
pos = starting_pos
dir = starting_dir

while within_map(map, pos[0], pos[1]):
    visited.add(pos)
    pos, dir = step(pos, dir, map, (-1, -1))

loop_obstacles = 0

for candidate_obstacle in visited:
    if candidate_obstacle == starting_pos:
        continue
    if is_loop(starting_pos, starting_dir, map, candidate_obstacle):
        loop_obstacles += 1

print(len(visited))
print(loop_obstacles)
