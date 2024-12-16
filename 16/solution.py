from sys import stdin
import heapq

maze = []

for line in stdin:
    maze.append(line.strip())

def rotate_l(dir):
    return (-dir[1], dir[0])

def rotate_r(dir):
    return (dir[1], -dir[0])

def add_vector(a, b):
    return (a[0] + b[0], a[1] + b[1])

def solve(maze):
    visit_queue = []
    visited = {}
    end_nodes = []
    heapq.heappush(visit_queue, (0, (len(maze) - 2, 1), (0 ,1), (-1, -1), (0, 0)))

    best_cost = -1

    while len(visit_queue) > 0:
        cost, pos, dir, prev_pos, prev_dir = heapq.heappop(visit_queue)

        if best_cost >= 0 and cost > best_cost:
            continue

        if maze[pos[0]][pos[1]] == 'E':
            end_nodes.append((pos, dir))
            best_cost = cost
        if maze[pos[0]][pos[1]] == '#':
            continue

        if (pos, dir) in visited:
            prev_cost, routes = visited[(pos, dir)]
            if cost > prev_cost:
                continue
            visited[(pos, dir)] = (cost, routes + [(prev_pos, prev_dir)])
        else:
            visited[(pos, dir)] = (cost, [(prev_pos, prev_dir)])

        heapq.heappush(visit_queue, (cost + 1, add_vector(pos, dir), dir, pos, dir))
        heapq.heappush(visit_queue, (cost + 1000, pos, rotate_l(dir), pos, dir))
        heapq.heappush(visit_queue, (cost + 1000, pos, rotate_r(dir), pos, dir))

    best_path_tile = set()
    visit_queue.extend(end_nodes)

    while len(visit_queue) > 0:
        pos, dir = visit_queue.pop()

        if (pos, dir) not in visited:
            continue
        best_path_tile.add(pos)

        _, routes = visited[pos, dir]
        del visited[pos, dir]
        visit_queue.extend(routes)

    return best_cost, len(best_path_tile)


print(solve(maze))
