with open("aoc-day-1-input.txt") as calibration_file:
    calibration = calibration_file.read()

calibration_list = calibration.splitlines()

num_words = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
)

part_one_total = 0
part_two_total = 0

for line in calibration_list:
    # Part One
    digits = [int(i) for i in line if i.isdigit()]
    part_one_total += int(str(digits[0]) + str(digits[-1]))

    # Part Two
    numbers = []
    for index, char in enumerate(line):
        if char.isdigit():
            numbers.append(char)
        else:
            for num, word in enumerate(num_words):
                if line[index : index + len(word)] == word:
                    numbers.append(str(num))
    part_two_total += int(numbers[0] + numbers[-1])

print(f"Part One Sum: {part_one_total}")
print(f"Part Two Sum: {part_two_total}")
