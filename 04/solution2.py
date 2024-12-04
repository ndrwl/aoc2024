from sys import stdin

data = []

def is_xmas(start_x, start_y):
    global data

    return (data[start_x][start_y] == 'A' and
        ((data[start_x - 1][start_y - 1] == 'M' and data[start_x + 1][start_y + 1] == 'S') or
         (data[start_x - 1][start_y - 1] == 'S' and data[start_x + 1][start_y + 1] == 'M')) and
        ((data[start_x - 1][start_y + 1] == 'M' and data[start_x + 1][start_y - 1] == 'S') or
         (data[start_x - 1][start_y + 1] == 'S' and data[start_x + 1][start_y - 1] == 'M')))

for line in stdin:
    data.append(line)

count = 0

for x in range(1, len(data) - 1):
    for y in range(1, len(data[0]) - 1):
        count += is_xmas(x, y)

print(count)
