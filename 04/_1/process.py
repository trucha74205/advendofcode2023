import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

def trim_and_parse_to_int(arr):
    print(f"Trimming and parsing: {arr}")
    return [int(elem.strip()) for elem in arr if elem.strip() != ""]

with open(file_path, "r") as file:
    for line in file:
        winning_numbers = line.split(":")[1].split("|")[0].split(" ")
        my_numbers = line.split(":")[1].split("|")[1].split(" ")

        winning_numbers = trim_and_parse_to_int(winning_numbers)
        my_numbers = trim_and_parse_to_int(my_numbers)

        power = -1

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                power += 1

        if power > -1:
            total_sum += 2 ** power


print(f"Total sum: {total_sum}")
print(f"Time elapsed: {time.time() - start_time} seconds")
