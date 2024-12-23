from sys import stdin

MAIN_KEYPAD = {
    '7': (0, 0),
    '8': (1 ,0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '#': (0, 3),
    '0': (1, 3),
    'A': (2, 3)
}

ARROW_KEYPAD = {
    '#': (0, 0),
    '^': (1, 0),
    'A': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1)
}

ARROW_DEPTH = 25

sum = 0

def options_for_key(keypad, start_key, end_key):
    start = keypad[start_key]
    end = keypad[end_key]
    blank = keypad['#']

    if start == end:
        return ['A']

    move = (end[0] - start[0], end[1] - start[1])

    path_x = ''
    path_y = ''

    if move[0] > 0:
        path_x += '>' * move[0]
    if move[0] < 0:
        path_x += '<' * -move[0]
    if move[1] > 0:
        path_y += 'v' * move[1]
    if move[1] < 0:
        path_y += '^' * -move[1]

    if move[0] == 0:
        return [path_y + 'A']
    if move[1] == 0:
        return [path_x + 'A']

    paths = []
    if not (start[0], end[1]) == blank:
        paths.append(path_y + path_x + 'A')
    if not (end[0], start[1]) == blank:
        paths.append(path_x + path_y + 'A')
    return paths

def shortest_route(route_map, keys):
    if len(route_map) == 0:
        return len(keys)

    current = 'A'

    length = 0
    for key in keys:
        length += route_map[(current, key)]
        current = key
    return length

def build_shortest_route_map(previous_map, keypad):
    route_map = {}
    for start_key in keypad:
        for end_key in keypad:
            route_map[(start_key, end_key)] = min([shortest_route(previous_map, keys)
                for keys in options_for_key(keypad, start_key, end_key)])
    return route_map

route_map = {}
for i in range(ARROW_DEPTH):
    route_map = build_shortest_route_map(route_map, ARROW_KEYPAD)
route_map = build_shortest_route_map(route_map, MAIN_KEYPAD)

for line in stdin:
    input = line.strip()
    sum += shortest_route(route_map, input) * int(input[:-1])

print(sum)
