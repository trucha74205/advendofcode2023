import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

lines = []


def getNumberAboveIndex(line, index):
    left_part = getNumberLeftFromIndex(line, index)
    right_part = getNumberRightFromIndex(line, index)
    complete_number = left_part if left_part != 0 else ""
    complete_number += line[index]
    complete_number += right_part if right_part != 0 else ""
    return int(complete_number)


def getNumberLeftFromIndex(line, index):
    number = ""
    i = index - 1
    while i >= 0 and line[i].isdigit():
        number = line[i] + number
        i -= 1
    return number if number != "" else 0


def getNumberRightFromIndex(line, index):
    number = ""
    i = index + 1
    while i < len(line) and line[i].isdigit():
        number += line[i]
        i += 1
    return number if number != "" else 0


def getNumbersFromNeighbouringLines(line, symbol_index):
    numbers = []
    if not line[symbol_index].isdigit():
        if (symbol_index - 1) >= 0:
            tmp_num = int(getNumberLeftFromIndex(line, symbol_index))
            numbers.append(tmp_num)
        if (symbol_index + 1) < len(line):
            tmp_num = int(getNumberRightFromIndex(line, symbol_index))
            numbers.append(tmp_num)
    else:
        numbers.append(getNumberAboveIndex(line, symbol_index))

    return numbers


def getNumbersForSymbolIndex(line, line_index, symbol_index):
    global total_sum
    numbers = []
    if line_index > 0:
        tmp_line = lines[line_index - 1]
        numbers = numbers + getNumbersFromNeighbouringLines(tmp_line, symbol_index)

    if (line_index + 1) < len(lines):
        tmp_line = lines[line_index + 1]
        numbers = numbers + getNumbersFromNeighbouringLines(tmp_line, symbol_index)

    numbers.append(int(getNumberLeftFromIndex(line, symbol_index)))
    numbers.append(int(getNumberRightFromIndex(line, symbol_index)))

    numbers = list(filter(lambda x: x != 0, numbers))

    if (len(numbers) == 2):
        product = 1
        for num in numbers:
            if num != 0:
                product *= num
        total_sum += product


with open(file_path, "r") as file:
    for line in file:
        lines.append(line)

for line_index, line in enumerate(lines):
    line = line.strip()
    for i in range(len(line)):
        if not line[i].isdigit() and line[i] != "." and line[i] == "*":
            getNumbersForSymbolIndex(line, line_index, i)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Total sum: {total_sum}")
