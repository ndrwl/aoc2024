from sys import stdin

first_list = []
second_list = []

for line in stdin:
    first, *_, second = line.split(' ')
    first_list.append(int(first))
    second_list.append(int(second))

first_list.sort()
second_list.sort()

total_distance = 0

for idx in range(len(first_list)):
    total_distance += abs(first_list[idx] - second_list[idx])

print(total_distance)
