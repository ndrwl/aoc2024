from sys import stdin

keys = []
locks = []

current_type = ''
current_line = 0
current = []

for line in stdin:
    line = line.strip()

    if current_type == '':
        if line == '.....':
            current_type = 'k'
            current = [5] * 5
            current_line = 0
        if line == '#####':
            current_type = 'l'
            current = [0] * 5
            current_line = 0
        continue

    if current_type == 'l':
        current_line += 1
        for i in range(5):
            if line[i] == '#':
                current[i] = current_line
        if current_line == 6:
            current_type = ''
            locks.append(current)
        continue

    if current_type == 'k':
        current_line += 1
        for i in range(5):
            if line[i] == '.':
                current[i] = 5 - current_line
        if current_line == 6:
            current_type = ''
            keys.append(current)
        continue

def fits(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

print(sum([fits(key, lock) for key in keys for lock in locks]))
