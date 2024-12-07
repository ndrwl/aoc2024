from sys import stdin

enable_concatenation = True
total_calibration_result = 0

def possible_results(possible_starts, numbers):
    global enable_concatenation

    if len(numbers) == 0:
        return possible_starts

    new_possible_starts = []

    for possible_start in possible_starts:
        new_possible_starts.append(possible_start * numbers[0])
        new_possible_starts.append(possible_start + numbers[0])

        if enable_concatenation:
            new_possible_starts.append(int(str(possible_start) + str(numbers[0])))

    return possible_results(new_possible_starts, numbers[1:])

for line in stdin:
    test_value_str, numbers_list_str = line.split(':')
    numbers_str = numbers_list_str.strip().split(' ')

    test_value = int(test_value_str)
    numbers = [int(number_str) for number_str in numbers_str]

    if test_value in possible_results([numbers[0]], numbers[1:]):
        total_calibration_result += test_value

print(total_calibration_result)
