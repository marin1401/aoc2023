#Day 09

with open('./10.txt') as my_input:
    input_lines = my_input.read().splitlines()

grid = [[char for char in chars] for chars in input_lines]

moves = {'N': {'|': 'N', '7': 'W', 'F': 'E'},
         'S': {'|': 'S', 'L': 'E', 'J': 'W'},
         'W': {'-': 'W', 'L': 'N', 'F': 'S'},
         'E': {'-': 'E', '7': 'S', 'J': 'N'}}

def find_start():
    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == 'S':
                return (y, x)

def shoelace_area(x, y):
    return abs( sum(i*j for i, j in zip(x, y[1:] + y[:1]))
               -sum(i*j for i, j in zip(x[1:] + x[:1], y)))//2

y, x = find_start()
tile = '.'
direction = 'S'
step = 0
coords = []
while tile != 'S':
    coords.append((y, x))
    if direction == 'N':
        y -= 1
    elif direction == 'S':
        y += 1
    elif direction == 'W':
        x -= 1
    elif direction == 'E':
        x += 1
    tile = grid[y][x]
    direction = moves[direction][tile] if tile != 'S' else direction
    step += 1

#Part 1

print(step//2)

#Part 2

y, x = zip(*coords)
print(shoelace_area(x, y) - len(coords)//2 + 1)