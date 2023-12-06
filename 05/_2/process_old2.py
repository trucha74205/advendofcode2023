import time

start_time = time.time()

file_path = "input.txt"
total_sum = 0

seedToSoil = dict()
soilToFertilizer = dict()
fertilizerToWater = dict()
waterToLight = dict()
lightToTemerature = dict()
tempToHumidity = dict()
humidityToLocation = dict()

seeds = []
locations = []
relSet = seedToSoil


def setRangeRelations(relationSet, sourceRangeStart, destRangeStart, rangeSize):
    sourceRangeStart = int(sourceRangeStart)
    destRangeStart = int(destRangeStart)
    rangeSize = int(rangeSize)
    for i in range(rangeSize):
        relationSet[sourceRangeStart + i] = destRangeStart + i


with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("seeds:"):
            seeds = line.split(":")[1].split(" ")
            continue
        elif line.startswith("seed-to-soil"):
            continue
        elif line.startswith("soil-to-fertilizer"):
            relSet = soilToFertilizer
            continue
        elif line.startswith("fertilizer-to-water"):
            relSet = fertilizerToWater
            continue
        elif line.startswith("water-to-light"):
            relSet = waterToLight
            continue
        elif line.startswith("light-to-temperature"):
            relSet = lightToTemerature
            continue
        elif line.startswith("temperature-to-humidity"):
            relSet = tempToHumidity
            continue
        elif line.startswith("humidity-to-location"):
            relSet = humidityToLocation
            continue

        parsed_line = line.split(" ")
        setRangeRelations(relSet, parsed_line[1], parsed_line[0], parsed_line[2])

print(f"Seeds: {seeds}")

for seed in seeds:
    if seed == "":
        continue
    seed = int(seed)
    soil = seedToSoil[seed] if seed in seedToSoil else seed
    fertilizer = soilToFertilizer[soil] if soil in soilToFertilizer else soil
    water = fertilizerToWater[fertilizer] if fertilizer in fertilizerToWater else fertilizer
    light = waterToLight[water] if water in waterToLight else water
    temperature = lightToTemerature[light] if light in lightToTemerature else light
    humidity = tempToHumidity[temperature] if temperature in tempToHumidity else temperature
    location = humidityToLocation[humidity] if humidity in humidityToLocation else humidity
    locations.append(int(location))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Lowest location: {min(locations)}")
