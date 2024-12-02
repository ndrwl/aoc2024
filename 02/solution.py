from sys import stdin

tolerate_bad_levels = True

def calculate_differences(levels):
    differences = []
    for idx in range(len(levels) - 1):
        differences.append(levels[idx + 1] - levels[idx])
    return differences

def is_safe(levels):
    differences = calculate_differences(levels)

    return (all(abs(diff) <= 3 for diff in differences) and
        (all(diff > 0 for diff in differences) or all(diff < 0 for diff in differences)))

def is_safe_with_tolerations(levels):
    for idx in range(len(levels)):
        level_copy = levels.copy()
        del level_copy[idx]
        if is_safe(level_copy):
            return True
    return False

safe_count = 0

for line in stdin:
    levels = [int(level_str) for level_str in line.split(' ')]
    if not tolerate_bad_levels:
        if is_safe(levels):
            safe_count += 1
    else:
        if is_safe_with_tolerations(levels):
            safe_count += 1

print(safe_count)
