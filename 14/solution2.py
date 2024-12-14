from sys import stdin
import re

MAX_X = 101
MAX_Y = 103

ADJACENT = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def pos_mod(x, r):
    return ((x % r) + r) % r

def solve(p_x, p_y, v_x, v_y, t):
    return (pos_mod(p_x + v_x * t, MAX_X), pos_mod(p_y + v_y * t, MAX_Y))

def count_contiguous(bot, bot_locations):
    initial_bot_count = len(bot_locations)
    visit_queue = [bot]

    while len(visit_queue) > 0:
        visitor = visit_queue.pop()
        for dir in ADJACENT:
            candidate = (visitor[0] + dir[0], visitor[1] + dir[1])
            if candidate not in bot_locations:
                continue
            bot_locations.remove(candidate)
            visit_queue.append(candidate)

    return initial_bot_count - len(bot_locations) + 1

def is_tree(bots):
    # If more than a quarter of the bots are grouped together consider it a tree
    bot_locations = set()

    for bot in bots:
        bot_locations.add((bot[0], bot[1]))

    while len(bot_locations) > 0:
        bot = bot_locations.pop()

        if count_contiguous(bot, bot_locations) > len(bots) // 4:
            return True
    return False

bots = []
seconds = 0

for line in stdin:
    matches = re.search(r'^p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)$', line.strip())
    if not matches:
        continue

    bots.append((int(matches.group(1)), int(matches.group(2)),
        int(matches.group(3)), int(matches.group(4))))

def step(t):
    global bots, seconds
    seconds += t

    for i in range(len(bots)):
        bot = bots[i]
        (new_x, new_y) = solve(bot[0], bot[1], bot[2], bot[3], t)
        bots[i] = (new_x, new_y, bot[2], bot[3])

def print_bots():
    global bots, seconds

    bot_locations = set()

    for bot in bots:
        bot_locations.add((bot[0], bot[1]))

    print(seconds, ' seconds:')

    for y in range(MAX_Y):
        line = ''
        for x in range(MAX_X):
            if (x, y) in bot_locations:
                line += 'X'
            else:
                line += ' '
        print(line)

while True:
    step(1)
    if is_tree(bots):
        break

print_bots()
