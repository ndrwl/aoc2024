from sys import stdin

towels_str = stdin.readline()
towels = [towel_str.strip() for towel_str in towels_str.split(',')]
stdin.readline()

def count_configurations(configuration):
    global towels

    counts = [1] + [0] * len(configuration)

    for start in range(len(configuration)):
        if counts[start] == 0:
            continue
        for towel in towels:
            if not configuration[start : start + len(towel)] == towel:
                continue
            counts[start + len(towel)] += counts[start]

    return counts[len(configuration)]

possible = 0
total_count = 0

for line in stdin:
    configuration = line.strip()
    count = count_configurations(configuration)

    possible += count > 0
    total_count += count

print(possible)
print(total_count)
