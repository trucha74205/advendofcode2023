import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def replace_words_with_digits(input_string, start_index=0):

    already_replaced = input_string[:start_index]
    string_to_analyse = input_string[start_index:]

    if string_to_analyse or len(string_to_analyse) > 2:
        if not string_to_analyse[0].isdigit():
            for word, digit in word_to_digit.items():
                if string_to_analyse.startswith(word):
                    string_to_analyse = digit + string_to_analyse[1:]
                    break
        return replace_words_with_digits(already_replaced+string_to_analyse, start_index + 1)
    else:
        return already_replaced + string_to_analyse

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespaces

        if line:
            line = replace_words_with_digits(line)

            # Find the first and last digits in the line
            all_digits_as_strings = [char for char in line if char.isdigit()]
            if len(all_digits_as_strings) > 0:
                total_sum += (int(all_digits_as_strings[0] + all_digits_as_strings[-1]))

end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Total sum of first and last digits: {total_sum}")
