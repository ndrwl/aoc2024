from sys import stdin

EMPTY_SPACE = '.'

resonant_frequency = True
map = []

for line in stdin:
    map.append(line.strip())

def within_map(map, node):
    return node[0] >= 0 and node[1] >= 0 and node[0] < len(map) and node[1] < len(map[0])

def add_nodes(a, b):
    return (a[0] + b[0], a[1] + b[1])

def subtract_nodes(a, b):
    return (a[0] - b[0], a[1] - b[1])

def calculate_antinodes(map, location1, location2):
    # 2B - A

    antinodes = []
    diff = subtract_nodes(location2, location1)
    antinode = add_nodes(location2, diff)

    while within_map(map, antinode):
        antinodes.append(antinode)

        if not resonant_frequency:
            break

        antinode = add_nodes(antinode, diff)

    return antinodes

antenna_locations = {}

for x in range(len(map)):
    for y in range(len(map[0])):
        if not map[x][y] == EMPTY_SPACE:
            antenna_type = map[x][y]
            antenna_locations.setdefault(antenna_type, []).append((x, y))

antinodes = set()

for antenna_type in antenna_locations:
    locations = antenna_locations[antenna_type]

    for location1 in locations:
        for location2 in locations:
            if location1 == location2:
                continue

            antinodes_a = calculate_antinodes(map, location1, location2)
            antinodes_b = calculate_antinodes(map, location2, location1)

            for antinode in antinodes_a:
                antinodes.add(antinode)
            for antinode in antinodes_b:
                antinodes.add(antinode)

            antinodes.add(location1)

print(len(antinodes))
