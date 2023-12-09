import time
import re

start_time = time.time()

file_path = "input.txt"
total_sum = 0
end_numbers = []
lines = []


def getNextNumber(numbers):
    new_numbers = []
    sum_of_new_numbers = 0
    for i in range(1, len(numbers)):
        diff = numbers[i-1] - numbers[i]
        new_numbers.append(diff)
        sum_of_new_numbers += diff
    if sum_of_new_numbers == 0:
        return new_numbers[-1]
    else:
        return new_numbers[-1] - getNextNumber(new_numbers)


with open(file_path, "r") as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    numbers = re.findall(r'-?\d+(?:\.\d+)?', line)
    numbers = list(map(int, numbers))
    numbers.reverse()

    number_to_add = getNextNumber(numbers)

    total_sum += numbers[-1] - number_to_add


end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Solution: {total_sum}")
