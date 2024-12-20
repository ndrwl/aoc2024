from sys import stdin

DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

grid = []

for line in stdin:
    grid.append(line.strip())

def find_char(grid, char):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == char:
                return (x, y)
    return (-1, -1)

def add_vector(a, b):
    return (a[0] + b[0], a[1] + b[1])

def within_grid(grid, pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid) and pos[1] < len(grid[0])

def bfs(grid, start, end):
    visit_map = {}
    visit_queue = [start]
    next_visit_queue = []
    current_length = 0

    while len(visit_queue) > 0:
        for pos in visit_queue:
            if pos in visit_map:
                continue
            visit_map[pos] = current_length

            if pos == end:
                return visit_map

            for dir in DIR:
                new_pos = add_vector(pos, dir)
                if not within_grid(grid, new_pos):
                    continue
                if grid[new_pos[0]][new_pos[1]] == '#':
                    continue
                next_visit_queue.append(new_pos)

        visit_queue = next_visit_queue
        next_visit_queue = []
        current_length += 1

    return {}

def iterate_cheat_dirs(cheat_length):
    cheat_dirs = [[(0, 0)]]
    visited = set()
    visited.add((0,0))

    for i in range(0, cheat_length):
        new_cheat_dirs = []
        for cheat_dir in cheat_dirs[i]:
            for dir in DIR:
                new_dir = add_vector(cheat_dir, dir)
                if new_dir in visited:
                    continue
                visited.add(new_dir)
                new_cheat_dirs.append(new_dir)
        cheat_dirs.append(new_cheat_dirs)
    return cheat_dirs

def count_cheat_solutions(visit_map_start, visit_map_end, max_cheat_length, min_time):
    cheat_dirs = iterate_cheat_dirs(max_cheat_length)

    count = 0

    for cheat_start, start_length in visit_map_start.items():
        for cheat_length in range(2, max_cheat_length + 1):
            for cheat_dir in cheat_dirs[cheat_length]:
                cheat_end = add_vector(cheat_start, cheat_dir)
                if not cheat_end in visit_map_end:
                    continue
                end_length = visit_map_end[cheat_end]
                total_length = start_length + cheat_length + end_length
                if total_length <= min_time:
                    count += 1

    return count

start = find_char(grid, 'S')
end = find_char(grid, 'E')

bfs_from_start = bfs(grid, start, end)
bfs_from_end = bfs(grid, end, start)
solution_length = bfs_from_start[end]

print(count_cheat_solutions(bfs_from_start, bfs_from_end, 2, solution_length - 100))
print(count_cheat_solutions(bfs_from_start, bfs_from_end, 20, solution_length - 100))
