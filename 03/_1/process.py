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
    sum_of_numbers = 0
    if not line[symbol_index].isdigit():
        if (symbol_index - 1) >= 0:
            # print("Found number diagonally top left")
            tmp_num = int(getNumberLeftFromIndex(line, symbol_index))
            sum_of_numbers += tmp_num
            # print(f"Number: {number}")
        if (symbol_index + 1) < len(line):
            # print("Found number diagonally top right")
            tmp_num = int(getNumberRightFromIndex(line, symbol_index))
            sum_of_numbers += tmp_num
            # print(f"Number: {number}")
    else:
        # print("Found number directly above")
        sum_of_numbers = getNumberAboveIndex(line, symbol_index)

    return sum_of_numbers


def getNumbersForSymbolIndex(line, line_index, symbol_index):
    global total_sum
    if line_index > 0:
        tmp_line = lines[line_index - 1]
        total_sum += getNumbersFromNeighbouringLines(tmp_line, symbol_index)

    if (line_index + 1) < len(lines):
        tmp_line = lines[line_index + 1]
        total_sum += getNumbersFromNeighbouringLines(tmp_line, symbol_index)

    number_before_symbol = int(getNumberLeftFromIndex(line, symbol_index))
    number_after_symbol = int(getNumberRightFromIndex(line, symbol_index))

    total_sum += number_before_symbol
    total_sum += number_after_symbol


with open(file_path, "r") as file:
    for line in file:
        lines.append(line)

for line_index, line in enumerate(lines):
    line = line.strip()
    for i in range(len(line)):
        if not line[i].isdigit() and line[i] != ".":
            getNumbersForSymbolIndex(line, line_index, i)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Total sum: {total_sum}")
