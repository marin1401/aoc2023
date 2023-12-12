#Day 05

with open('./05.txt') as my_input:
    input_lines = my_input.readlines()

seeds = map(int, input_lines[0].split()[1:])

maps = {}
for line in input_lines:
    if len(line.split()) == 2:
        map_name = line.split()[0]
        maps[map_name] = []
    elif len(line.split()) == 3:
        maps[map_name].append(tuple(map(int, line.split())))

locations = set()
for seed in seeds:
    for ranges in maps.values():
        for destination, source, range_length in ranges:
            if seed in range(source, source + range_length):
                seed = destination + seed - source
                break
    locations.add(seed)

print(min(locations))
