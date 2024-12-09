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

free_space_pointer = 0
block_pointer = len(blocks) - 1

while block_pointer > free_space_pointer:
    if blocks[free_space_pointer] != -1:
        free_space_pointer += 1
        continue
        
    if blocks[block_pointer] != -1:
        blocks[free_space_pointer] = blocks[block_pointer]
        blocks[block_pointer] = -1

    block_pointer -= 1

checksum = 0

for pos in range(len(blocks)):
    if blocks[pos] != -1:
        checksum += pos * blocks[pos]

print(checksum)
