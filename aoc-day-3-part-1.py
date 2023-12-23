import numpy as np

def isValidPos(i, j, n, m):

    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

def getAdjacent(arr, i, j):

    # Size of given 2d array
    n = len(arr)
    m = len(arr[0])

    # Initialising a vector array
    # where adjacent element will be stored
    v = []

    # Checking for all the possible adjacent positions
    if (isValidPos(i - 1, j - 1, n, m)):
        v.append(arr[i - 1][j - 1])
    if (isValidPos(i - 1, j, n, m)):
        v.append(arr[i - 1][j])
    if (isValidPos(i - 1, j + 1, n, m)):
        v.append(arr[i - 1][j + 1])
    if (isValidPos(i, j - 1, n, m)):
        v.append(arr[i][j - 1])
    if (isValidPos(i, j + 1, n, m)):
        v.append(arr[i][j + 1])
    if (isValidPos(i + 1, j - 1, n, m)):
        v.append(arr[i + 1][j - 1])
    if (isValidPos(i + 1, j, n, m)):
        v.append(arr[i + 1][j])
    if (isValidPos(i + 1, j + 1, n, m)):
        v.append(arr[i + 1][j + 1])

    # Returning the vector
    return v

with open("aoc-day-3-input.txt") as machine_parts_file:
    machine_parts = machine_parts_file.read()

machine_parts_lines = machine_parts.splitlines()

padded_matrix = []
for line in machine_parts_lines:
    line = "." + line + "."
    padded_matrix.append(line)

padded_matrix.append("." * len(padded_matrix[0]))
padded_matrix.insert(0, ("." * len(padded_matrix[0])))

# Part One
all_nums = []
line_numbers = set()
same_number = False

for i in range(0, (len(padded_matrix))):
    line_numbers = []
    for j in range(0, (len(padded_matrix[0]))):
        number = []
        if not padded_matrix[i][j].isnumeric():
            same_number = False

        adjacent = (getAdjacent(padded_matrix, i, j))
        is_part = False

        for char in adjacent:
            if padded_matrix[i][j].isnumeric() and not char.isalnum() and not char == "." and not is_part and not same_number:
                is_part = True
                same_number = True
                break

        left_neighbours = True
        right_neighbours = True

        if is_part:
            while left_neighbours and right_neighbours:
                for n in reversed(range(0, j)):
                    if padded_matrix[i][n].isnumeric():
                        number.insert(0, padded_matrix[i][n])
                    else:
                        left_neighbours = False
                        break
                for m in range(j, (len(padded_matrix)-1)):
                    if padded_matrix[i][m].isnumeric():
                        number.append(padded_matrix[i][m])
                    else:
                        right_neighbours = False
                        break

            line_numbers.append(int(''.join(number)))
    all_nums.extend(line_numbers)

print(f"Part One Total: {sum(all_nums)}")
