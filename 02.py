#Day 02

with open('./02.txt') as my_input:
    input_lines = my_input.read().splitlines()

games = [game.split(': ')[1:][0].split('; ') for game in input_lines]
cubes_in_a_game = {'red': 12, 'green': 13, 'blue': 14}

counter = 1
id_sum = 0
power_sum = 0
for game in games:
    possible = True
    fewest_cubes_in_a_game = {'red': 0, 'green': 0, 'blue': 0}
    for subgame in game:
        cubes = subgame.split(', ')
        for cube in cubes:
            number, colour = cube.split()
            if cubes_in_a_game[colour] < int(number):
                possible = False
            if fewest_cubes_in_a_game[colour] < int(number):
                fewest_cubes_in_a_game[colour] = int(number)
    if possible:
        id_sum += counter
    power = 1
    for value in fewest_cubes_in_a_game.values():
        power *= value
    power_sum += power
    counter += 1

#Part 1

print(id_sum)

#Part 2

print(power_sum)