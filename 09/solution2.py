from sys import stdin

blocks = []

block_id = 0
is_block = True

for line in stdin:
    for char in line.strip():
        if is_block:
            blocks.extend([block_id] * int(char))
            block_id += 1
        else:
            blocks.extend([-1] * int(char))
        is_block = not is_block

def calc_free_space_size(blocks, pointer):
    size = 0
    while pointer < len(blocks) and blocks[pointer + size] == -1:
        size += 1
    return size

def calc_block_size(blocks, pointer):
    size = 0
    while pointer >= 0 and blocks[pointer - size] == blocks[pointer]:
        size += 1
    return size

block_pointer = len(blocks) - 1

while block_pointer >= 0:
    if blocks[block_pointer] == -1:
        block_pointer -= 1
        continue

    block_size = calc_block_size(blocks, block_pointer)

    free_space_pointer = 0

    while free_space_pointer < block_pointer:
        if blocks[free_space_pointer] != -1:
            free_space_pointer += 1
            continue

        free_space_size = calc_free_space_size(blocks, free_space_pointer)

        if block_size <= free_space_size:
            block_id = blocks[block_pointer]
            for offset in range(block_size):
                blocks[free_space_pointer + offset] = block_id
                blocks[block_pointer - offset] = -1
            break

        free_space_pointer += free_space_size

    block_pointer -= block_size

checksum = 0

for pos in range(len(blocks)):
    if blocks[pos] != -1:
        checksum += pos * blocks[pos]

print(checksum)
