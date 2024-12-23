from sys import stdin
from collections import defaultdict

neighbours = defaultdict(set)

for line in stdin:
    computer1, computer2 = line.strip().split('-')

    if computer1 < computer2:
        neighbours[computer1].add(computer2)
        neighbours[computer2]
    else:
        neighbours[computer2].add(computer1)
        neighbours[computer1]

def iterate_group(neighbours, groups, current_group):
    groups.append(current_group)

    for candidate in neighbours[current_group[-1]]:
        if not all([candidate in neighbours[member] for member in current_group]):
            continue
        iterate_group(neighbours, groups, current_group.copy() + [candidate])

def list_groups(neighbours):
    groups = []

    for computer1 in neighbours:
        iterate_group(neighbours, groups, [computer1])

    return groups

def contains_t(triple):
    return triple[0][0] == 't' or triple[1][0] == 't' or triple[2][0] == 't'

groups = list_groups(neighbours)

print(sum(1 if len(group) == 3 and contains_t(group) else 0 for group in groups))
print(','.join(max(groups, key=lambda group: len(group))))
