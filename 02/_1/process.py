import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

color_max = dict({
    "blue": 14,
    "red": 12,
    "green": 13
})

games = []
sum = 0

def parseAndAddGameData(line):
    global sum
    colors = dict({
        "blue": [],
        "red": [],
        "green": []
    })
    game_number = int(line.split(":")[0].split(" ")[1].strip())
    draws = line.split(":")[1].split(";")
    for draw in draws:
        drawn_colors = draw.split(",")
        for drawn_color in drawn_colors:
            draw_amount = int(drawn_color.strip().split(" ")[0].strip())
            draw_color = drawn_color.strip().split(" ")[1].strip()
            if draw_amount > color_max[draw_color]:
                return
            colors[draw_color].append(draw_amount)
    sum += game_number
    games.append(colors)



with open(file_path, "r") as file:
    for line in file:
        parseAndAddGameData(line)

print(games)

print(f"Total sum: {sum}")
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
