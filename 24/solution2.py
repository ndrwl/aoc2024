from sys import stdin
import re

operations = []

for line in stdin:
    operation_match = re.search(r'^([a-z0-9]{3}) (AND|OR|XOR) ([a-z0-9]{3}) -> ([a-z0-9]{3})\n$', line)
    if operation_match:
        operations.append((operation_match.group(1), operation_match.group(2), operation_match.group(3), operation_match.group(4)))

def wire_name(prefix, bit):
    return '%s%02d' % (prefix, bit)

def int_to_wire_values(prefix, value, max_bit):
    wire_values = {}
    for bit_position in range(max_bit + 1):
        wire_values[wire_name(prefix, bit_position)] = bool(value % 2)
        value = value >> 1

    return wire_values

def z_value(wire_values):
    z = 0
    for wire in wire_values:
        if not wire[0] == 'z':
            continue
        z += wire_values[wire] << int(wire[1:])
    return z

def execute(x, y, operations, swaps, max_bit):
    wire_values = {}
    wire_values.update(int_to_wire_values('x', x, max_bit))
    wire_values.update(int_to_wire_values('y', y, max_bit))

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

            if out in swaps:
                out = swaps[out]
            if op == 'AND':
                wire_values[out] = wire_values[in1] & wire_values[in2]
            if op == 'OR':
                wire_values[out] = wire_values[in1] | wire_values[in2]
            if op == 'XOR':
                wire_values[out] = wire_values[in1] ^ wire_values[in2]
    return z_value(wire_values)

def calc_output_dependencies_for_input(operations, wire):
    dependencies = set()
    dependencies.add(wire)

    new_dependencies = True
    while new_dependencies:
        new_dependencies = False
        for (in1, _, in2, out) in operations:
            if out not in dependencies:
                continue
            if in1 not in dependencies:
                dependencies.add(in1)
                new_dependencies = True
            if in2 not in dependencies:
                dependencies.add(in2)
                new_dependencies = True

    output_dependencies = []
    for (_, _, _, out) in operations:
        if out in dependencies:
            output_dependencies.append(out)

    return output_dependencies

def calc_output_dependencies_for_output(operations, wire):
    dependencies = set()
    dependencies.add(wire)

    new_dependencies = True
    while new_dependencies:
        new_dependencies = False
        for (in1, _, in2, out) in operations:
            if in1 not in dependencies and in2 not in dependencies:
                continue
            if out not in dependencies:
                dependencies.add(out)
                new_dependencies = True

    output_dependencies = []
    for (_, _, _, out) in operations:
        if out in dependencies:
            output_dependencies.append(out)

    return output_dependencies

def attempt_swap(operations, bit, max_bit, swaps, fixed):
    dependencies = calc_output_dependencies_for_input(operations, wire_name('z', bit))

    for candidate1 in dependencies:
        if candidate1 in fixed:
            continue
        for (_, _, _, candidate2) in operations:
            if candidate2 in fixed or candidate2 == candidate1:
                continue

            new_swaps = swaps.copy()

            new_swaps[candidate1] = candidate2
            new_swaps[candidate2] = candidate1

            if not test(operations, bit, new_swaps):
                continue

            new_fixed = fixed.copy()

            new_fixed.add(candidate1)
            new_fixed.add(candidate2)

            attempt = solve(operations, bit, max_bit, new_swaps, new_fixed)
            if attempt != False:
                return attempt

    return False

TESTS = [(0, 0), (2, 0), (0, 2), (1, 1), (3, 1), (1, 3)]

def test(operations, bit, swaps):
    mask = (1 << bit + 1) - 1
    for test_x, test_y in TESTS:
        x = (test_x << bit) >> 1
        y = (test_y << bit) >> 1
        z = (x + y) & mask

        if not execute(x, y, operations, swaps, bit) & mask == z:
            return False
    return True

def solve(operations, start_bit, max_bit, swaps, fixed):
    for bit in range(start_bit, max_bit):
        # ensure that this bit works
        if test(operations, bit, swaps):
            fixed.update(calc_output_dependencies_for_input(operations, wire_name('z', bit)))
            continue

        if len(swaps) == 8:
            return False

        # bit does not work, try swap
        return attempt_swap(operations, bit, max_bit, swaps, fixed)

    return swaps

swaps = solve(operations, 0, 44, {}, set())
print(','.join(sorted(swaps.keys())))
