from sys import stdin

data = []

def is_valid_coordinate(x, y):
    global data

    return x >= 0 and y >= 0 and x < len(data) and y < len(data[0])

def is_xmas(start_x, start_y, dir_x, dir_y):
    global data

    if not is_valid_coordinate(start_x + dir_x * 3, start_y + dir_y * 3):
        return False

    return (data[start_x][start_y] == 'X' and
        data[start_x + dir_x][start_y + dir_y] == 'M' and
        data[start_x + dir_x * 2][start_y + dir_y * 2] == 'A' and
        data[start_x + dir_x * 3][start_y + dir_y * 3] == 'S')

for line in stdin:
    data.append(line)

count = 0

for x in range(len(data)):
    for y in range(len(data[0])):
        for dir_x in range(-1,2):
            for dir_y in range(-1,2):
                count += is_xmas(x, y, dir_x, dir_y)

print(count)
