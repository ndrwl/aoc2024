from sys import stdin
import re

a_match = re.search(r'^Register A: ([\d]*)\n$', stdin.readline())
b_match = re.search(r'^Register B: ([\d]*)\n$', stdin.readline())
c_match = re.search(r'^Register C: ([\d]*)\n$', stdin.readline())
stdin.readline()
program_match = re.search(r'^Program: ([\d,]*)\n$', stdin.readline())

init_a = int(a_match.group(1))
init_b = int(b_match.group(1))
init_c = int(c_match.group(1))

program = [int(instruction_str) for instruction_str in program_match.group(1).split(',')]

def combo(operand, a, b, c):
    if operand < 4:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    return 0

def test(program, a, b, c, expected):
    pointer = 0
    out_pointer = 0

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]

        if instruction == 0:
            a = a >> combo(operand, a, b, c)
        elif instruction == 1:
            b = b ^ operand
        elif instruction == 2:
            b = combo(operand, a, b, c) % 8
        elif instruction == 3:
            if not a == 0:
                pointer = operand
                continue
        elif instruction == 4:
            b = b ^ c
        elif instruction == 5:
            out = combo(operand, a, b, c) % 8
            if out_pointer >= len(expected) or expected[out_pointer] != out:
                out_pointer = 0
                break
            out_pointer += 1
        elif instruction == 6:
            b = a >> combo(operand, a, b, c)
        elif instruction == 7:
            c = a >> combo(operand, a, b, c)

        pointer += 2

    return out_pointer == len(expected)

match_length = 0
candidates = [0]

while match_length < len(program):
    # Add 3 bits at a time to each of the candidates
    match_length += 1
    new_candidates = []

    for candidate in candidates:
        candidate_shifted = candidate << 3
        for extra_bits in range(8):
            new_candidate = candidate_shifted + extra_bits

            if test(program, new_candidate, init_b, init_c, program[-match_length:]):
                new_candidates.append(new_candidate)

    candidates = new_candidates

print(candidates[0])
