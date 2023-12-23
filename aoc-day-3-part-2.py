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
        v.append([arr[i - 1][j - 1],i-1,j-1])
    if (isValidPos(i - 1, j, n, m)):
        v.append([arr[i - 1][j],i-1,j])
    if (isValidPos(i - 1, j + 1, n, m)):
        v.append([arr[i - 1][j + 1], i-1, j+1])
    if (isValidPos(i, j - 1, n, m)):
        v.append([arr[i][j - 1], i, j-1])
    if (isValidPos(i, j + 1, n, m)):
        v.append([arr[i][j + 1], i, j+1])
    if (isValidPos(i + 1, j - 1, n, m)):
        v.append([arr[i + 1][j - 1], i+1, j-1])
    if (isValidPos(i + 1, j, n, m)):
        v.append([arr[i + 1][j], i+1, j])
    if (isValidPos(i + 1, j + 1, n, m)):
        v.append([arr[i + 1][j + 1], i+1, j+1])

    # Returning the vector
    return v

# Part Two
with open("aoc-day-3-input.txt") as machine_parts_file:
    machine_parts = machine_parts_file.read()

machine_parts_lines = machine_parts.splitlines()

padded_matrix = []
for line in machine_parts_lines:
    line = "." + line + "."
    padded_matrix.append(line)

padded_matrix.append("." * len(padded_matrix[0]))
padded_matrix.insert(0, ("." * len(padded_matrix[0])))

total = 0
for i in range(0, (len(padded_matrix))):
    for j in range(0, (len(padded_matrix[0]))):
        if padded_matrix[i][j] == "*":
            adjacent = getAdjacent(padded_matrix, i, j)
            gear_numbers = set()
            number = []
            for item in adjacent:
                if item[0].isnumeric():
                    number = []
                    left_neighbours = True
                    right_neighbours = True
                    i1 = item[1]
                    j1 = item[2]
                    while left_neighbours and right_neighbours:
                        for n in reversed(range(0, j1)):
                            if padded_matrix[i1][n].isnumeric():
                                number.insert(0, padded_matrix[i1][n])
                            else:
                                left_neighbours = False
                                break
                        for m in range(j1, (len(padded_matrix)-1)):
                            if padded_matrix[i1][m].isnumeric():
                                number.append(padded_matrix[i1][m])
                            else:
                                right_neighbours = False
                                break

                if number:
                    gear_numbers.add(int(''.join(number)))

            if len(gear_numbers) == 2:
                gear_numbers = list(gear_numbers)
                product = gear_numbers[0]*gear_numbers[1]
                total += product
print(f"Total: {total}")
