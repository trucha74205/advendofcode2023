import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0


def trim_and_parse_to_int(arr):
    return [int(elem.strip()) for elem in arr if elem.strip() != ""]


copies = [0]
i = -1
with open(file_path, "r") as file:
    for line in file:
        i += 1
        winning_numbers = line.split(":")[1].split("|")[0].split(" ")
        my_numbers = line.split(":")[1].split("|")[1].split(" ")

        winning_numbers = trim_and_parse_to_int(winning_numbers)
        my_numbers = trim_and_parse_to_int(my_numbers)
        winners = 0

        for winning_number in winning_numbers:
            if winning_number in my_numbers:
                winners += 1

        if winners == 0:
            copies.append(0)

        for n in range(winners):
            if (i+n+1) < len(copies):
                copies[i+n+1] += 1*(copies[i]+1)
            else:
                copies.append((copies[i]+1))

print(f"Total sum: {sum(copies) + i + 1}")
print(f"Time elapsed: {time.time() - start_time} seconds")
