from sys import stdin

PRUNE_AND = 16777215

def generate(secret, iterations):
    for i in range(iterations):
        secret = (secret ^ secret << 6) & PRUNE_AND
        secret = (secret ^ secret >> 5) & PRUNE_AND
        secret = (secret ^ secret << 11) & PRUNE_AND
    return secret

sum = 0

for line in stdin:
    seed = int(line)
    sum += generate(seed, 2000)

print(sum)
