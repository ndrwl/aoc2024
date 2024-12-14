from sys import stdin
import re

MAX_X = 101
MAX_Y = 103
T = 100

def pos_mod(x, r):
    return ((x % r) + r) % r

def solve(p_x, p_y, v_x, v_y, t):
    return (pos_mod(p_x + v_x * t, MAX_X), pos_mod(p_y + v_y * t, MAX_Y))

def quad_id(x, y):
    if x < MAX_X // 2 and y < MAX_Y // 2:
        return 0
    if x < MAX_X // 2 and y > MAX_Y // 2:
        return 1
    if x > MAX_X // 2 and y < MAX_Y // 2:
        return 2
    if x > MAX_X // 2 and y > MAX_Y // 2:
        return 3
    return 4

quad_count = [0, 0, 0, 0, 0]

for line in stdin:
    matches = re.search(r'^p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)$', line.strip())
    if not matches:
        continue

    (x, y) = solve(int(matches.group(1)), int(matches.group(2)),
        int(matches.group(3)), int(matches.group(4)), T)

    quad_count[quad_id(x,  y)] += 1

print(quad_count[0] * quad_count[1] * quad_count[2] * quad_count[3])
