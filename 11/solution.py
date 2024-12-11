from sys import stdin
from collections import defaultdict

stones = []

for line in stdin:
    numbers_str = line.strip().split(' ')
    stones.extend([int(number_str) for number_str in numbers_str])

def num_digits(number):
    digits = 1
    if number >= 100000000:
        digits += 8
        number //= 100000000
    if number >= 10000:
        digits += 4
        number //= 10000
    if number >= 100:
        digits += 2
        number //= 100
    if number >= 10:
        digits += 1
    return digits

def iterate(stones):
    new_stones = defaultdict(int)

    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
            continue

        if num_digits(stone) % 2 == 0:
            stone_str = str(stone)
            half_len = len(stone_str) // 2
            new_stones[int(stone_str[:half_len])] += count
            new_stones[int(stone_str[half_len:])] += count
            continue

        new_stones[stone * 2024] += count

    return new_stones

stone_number_count = defaultdict(int)

for stone in stones:
    stone_number_count[stone] += 1

for iteration in range(75):
    stone_number_count = iterate(stone_number_count)

stone_count = sum(stone_number_count.values())
print(stone_count)
