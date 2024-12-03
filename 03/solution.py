from sys import stdin
import re

enable_dos = True
sum = 0
bool_is_enabled = True

for line in stdin:
    instructions = re.findall(r'(?:mul\(([0-9]{1,3}\,[0-9]{1,3})\))|(do\(\))|(don\'t\(\))', line)

    for (mul_instruction, do_instruction, dont_instruction) in instructions:

        if do_instruction:
            if enable_dos:
                bool_is_enabled = True

        elif dont_instruction:
            if enable_dos:
                bool_is_enabled = False

        elif bool_is_enabled:
            x_str, y_str = mul_instruction.split(',')
            sum += int(x_str) * int(y_str)

print(sum)
