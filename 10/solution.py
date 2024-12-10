from sys import stdin

map = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for line in stdin:
    map.append([int(height_str) for height_str in line.strip()])

def within_map(map, x, y):
    return x >= 0 and y >= 0 and x < len(map) and y < len(map[0])

def get_peaks(map, x, y):
    height = map[x][y]

    if height == 9:
        return 1, set([(x, y)])

    count = 0
    peaks = set()
    for direction in directions:
        if not within_map(map, x + direction[0], y + direction[1]):
            continue
        if map[x + direction[0]][y + direction[1]] == height + 1:
            new_count, new_peaks = get_peaks(map, x + direction[0], y + direction[1])
            count += new_count
            peaks.update(new_peaks)
    return count, peaks

total_trails = 0
total_peaks = 0

for x in range(len(map)):
    for y in range(len(map[0])):
        if map[x][y] == 0:
            trail_count, peak_set = get_peaks(map, x, y)
            total_trails += trail_count
            total_peaks += len(peak_set)

print(total_peaks)
print(total_trails)
