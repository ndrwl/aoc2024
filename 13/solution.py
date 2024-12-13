from sys import stdin
import re

OFFSET = 10000000000000

lines = []

for line in stdin:
    lines.append(line.strip())

def solve(a_x, a_y, b_x, b_y, prize_x, prize_y):
    # Solve simultaneous equation:
    # (a_x * b_y - a_y * b_x) a = (prize_x * b_y - prize_y * b_x)

    divisor = a_x * b_y - a_y * b_x
    if divisor == 0:
        # a and b are parallel, solve just for b
        b = prize_x // b_x
        if b_x * b == prize_x and b_y * b == prize_y:
            return b
        return 0

    dividend = prize_x * b_y - prize_y * b_x

    if dividend % divisor != 0:
        return 0
    a = dividend // divisor

    if (prize_x - a * a_x) % b_x != 0:
        return 0
    b = (prize_x - a * a_x) // b_x

    return 3 * a + b

total_cost = 0

for i in range((len(lines) + 1) // 4):
    button_a_match = re.search(r'^Button A: X\+([\d]*), Y\+([\d]*)$', lines[i*4 + 0])
    button_b_match = re.search(r'^Button B: X\+([\d]*), Y\+([\d]*)$', lines[i*4 + 1])
    prize_match    = re.search(r'^Prize: X\=([\d]*), Y\=([\d]*)$', lines[i*4 + 2])

    total_cost += solve(int(button_a_match.group(1)), int(button_a_match.group(2)),
        int(button_b_match.group(1)), int(button_b_match.group(2)),
        OFFSET + int(prize_match.group(1)), OFFSET + int(prize_match.group(2)))

print(total_cost)
