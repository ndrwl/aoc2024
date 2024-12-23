from sys import stdin
from collections import defaultdict

PRUNE_AND = 16777215

def calculate_prices(secret, iterations):
    prices = [secret % 10]
    for i in range(iterations):
        secret = (secret ^ secret << 6) & PRUNE_AND
        secret = (secret ^ secret >> 5) & PRUNE_AND
        secret = (secret ^ secret << 11) & PRUNE_AND
        prices.append(secret % 10)
    return prices

def update_cost_sequences(cost_sequences, prices):
    seen = set()

    diff = (0, prices[1] - prices[0], prices[2] - prices[1], prices[3] - prices[2])

    for i in range(4, len(prices)):
        diff = (diff[1], diff[2], diff[3], prices[i] - prices[i-1])

        if diff in seen:
            continue
        seen.add(diff)

        cost_sequences[diff] += prices[i]

cost_sequences = defaultdict(int)

for line in stdin:
    seed = int(line)
    update_cost_sequences(cost_sequences, calculate_prices(seed, 2000))

print(max(cost_sequences.values()))
