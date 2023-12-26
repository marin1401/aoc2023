#Day 05

with open('./05.txt') as my_input:
    input_lines = my_input.readlines()

seeds = list(map(int, input_lines[0].split()[1:]))

maps = {}
for line in input_lines:
    if len(line.split()) == 2:
        map_name = line.split()[0]
        maps[map_name] = []
    elif len(line.split()) == 3:
        maps[map_name].append(tuple(map(int, line.split())))

#Part 1

min_value = max(seeds)
for seed in seeds:
    value = seed
    for ranges in maps.values():
        for destination, source, range_length in ranges:
            if source <= value < source + range_length:
                value = destination + value - source
                break
    min_value = value if value < min_value else min_value

print(min_value)

#Part 2

pairs = [(start, start + rng) for start, rng in zip(seeds[::2], seeds[1::2])]

def get_lowest_location():
    for min_location in range(max(seeds)):
        value = min_location
        for ranges in reversed(list(maps.values())):
            for destination, source, range_length in ranges:
                if destination <= value < destination + range_length:
                    value = source + value - destination
                    break
        for min_seed, max_seed in pairs:
            if min_seed <= value <= max_seed:
                return min_location

print(get_lowest_location())