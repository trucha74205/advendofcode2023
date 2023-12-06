import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespaces

        if line:
            all_digits_as_strings = [char for char in line if char.isdigit()]
            if len(all_digits_as_strings) > 0:
                total_sum += (int(all_digits_as_strings[0] + all_digits_as_strings[-1]))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Total sum of first and last digits: {total_sum}")
