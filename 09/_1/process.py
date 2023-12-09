import time
import re

start_time = time.time()

file_path = "input.txt"
total_sum = 0
end_numbers = []
lines = []


def getNextNumber(numbers, next_number=0):
    new_numbers = []
    sum_of_new_numbers = 0
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        new_numbers.append(diff)
        sum_of_new_numbers += diff
    if sum_of_new_numbers == 0:
        return next_number
    else:
        return getNextNumber(new_numbers, next_number + new_numbers[-1])


with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    numbers = re.findall(r'-?\d+(?:\.\d+)?', line)
    numbers = list(map(int, numbers))

    number_to_add = getNextNumber(numbers)

    total_sum += numbers[-1] + number_to_add


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Solution: {total_sum}")
