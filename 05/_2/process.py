import time
import concurrent.futures

start_time = time.time()

file_path = "input.txt"
total_sum = 0

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemerature = []
tempToHumidity = []
humidityToLocation = []

seeds = []
locations = []
relSet = seedToSoil


def getMappingForNumber(relSet, number):
    for relationTuple in relSet:
        if relationTuple[0] <= number <= (relationTuple[0] + relationTuple[2] - 1):
            return relationTuple[1] + abs(relationTuple[0] - number)
    return number


def getLocationsForSeeds(seed):
    soil = getMappingForNumber(seedToSoil, seed)
    fertilizer = getMappingForNumber(soilToFertilizer, soil)
    water = getMappingForNumber(fertilizerToWater, fertilizer)
    light = getMappingForNumber(waterToLight, water)
    temperature = getMappingForNumber(lightToTemerature, light)
    humidity = getMappingForNumber(tempToHumidity, temperature)
    location = getMappingForNumber(humidityToLocation, humidity)

    # locations.append(int(location))
    return int(location)


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
        parsed_line = [int(value) for value in parsed_line if value.strip() != ""]

        relSet.append([parsed_line[1], parsed_line[0], parsed_line[2]])

seeds = [int(value) for value in seeds if value.strip() != ""]
for i in range(0, 2, 2):
    # for i in range(0, len(seeds), 2):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        locations.append(list(executor.map(getLocationsForSeeds, [seeds[i]+j for j in range(seeds[i+1])])))

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Time taken: {elapsed_time} seconds")
print(f"Lowest location: {min(locations)}")
