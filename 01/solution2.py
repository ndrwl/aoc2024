from sys import stdin

first_list = []
second_list_occurences = {}

for line in stdin:
    first, *_, second = line.split(' ')
    first_list.append(int(first))

    second_int = int(second)
    second_list_occurences.setdefault(second_int, 0)
    second_list_occurences[second_int] += 1

similarity = 0

for first in first_list:
    similarity += first * second_list_occurences.setdefault(first, 0)

print(similarity)
