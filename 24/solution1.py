from sys import stdin
import re

wire_values = {}
operations = []

for line in stdin:
    init_match = re.search(r'^([xy]\d\d): ([01])\n$', line)
    if init_match:
        wire_values[init_match.group(1)] = bool(int(init_match.group(2)))
        continue

    operation_match = re.search(r'^([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})\n$', line)
    if operation_match:
        operations.append((operation_match.group(1), operation_match.group(2), operation_match.group(3), operation_match.group(4)))

def execute(wire_values, operations):
    executed = True
    operations_executed = set()

    while executed:
        executed = False

        for i in range(len(operations)):
            if i in operations_executed:
                continue

            in1, op, in2, out = operations[i]
            if not in1 in wire_values or not in2 in wire_values:
                continue

            executed = True
            operations_executed.add(i)

            if op == 'AND':
                wire_values[out] = wire_values[in1] & wire_values[in2]
            if op == 'OR':
                wire_values[out] = wire_values[in1] | wire_values[in2]
            if op == 'XOR':
                wire_values[out] = wire_values[in1] ^ wire_values[in2]

def z_value(wire_values):
    z = 0
    for wire in wire_values:
        if not wire[0] == 'z':
            continue
        z += wire_values[wire] << int(wire[1:])
    return z

execute(wire_values, operations)
print(z_value(wire_values))
