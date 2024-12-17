from sys import stdin
import re

a_match = re.search(r'^Register A: ([\d]*)\n$', stdin.readline())
b_match = re.search(r'^Register B: ([\d]*)\n$', stdin.readline())
c_match = re.search(r'^Register C: ([\d]*)\n$', stdin.readline())
stdin.readline()
program_match = re.search(r'^Program: ([\d,]*)\n$', stdin.readline())

a = int(a_match.group(1))
b = int(b_match.group(1))
c = int(c_match.group(1))

program = [int(instruction_str) for instruction_str in program_match.group(1).split(',')]

pointer = 0

def combo(operand):
    if operand < 4:
        return operand
    if operand == 4:
        return a
    if operand == 5:
        return b
    if operand == 6:
        return c
    return 0

out = []

while pointer < len(program):
    instruction = program[pointer]
    operand = program[pointer + 1]

    if instruction == 0:
        a = a >> combo(operand)
    elif instruction == 1:
        b = b ^ operand
    elif instruction == 2:
        b = combo(operand) % 8
    elif instruction == 3:
        if not a == 0:
            pointer = operand
            continue
    elif instruction == 4:
        b = b ^ c
    elif instruction == 5:
        out.append(combo(operand) % 8)
    elif instruction == 6:
        b = a >> combo(operand)
    elif instruction == 7:
        c = a >> combo(operand)

    pointer += 2

print(','.join([str(i) for i in out]))
