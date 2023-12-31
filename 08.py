#Day 08

from math import lcm

with open('./08.txt') as my_input:
    input_lines = my_input.read()

instructions, nodes = input_lines.split('\n\n')
nodes = {node[:3]: (node[7:10] , node[12:15])for node in nodes.splitlines()}

def calculate_steps(positions, part):
    steps = []
    for position in positions:
        end = False
        step = 0
        while not end:
            for instruction in instructions:
                if instruction == 'L':
                    position = nodes[position][0]
                elif instruction == 'R':
                    position = nodes[position][1]
                step += 1
                if position == 'ZZZ' and part == 1 or position[2] == 'Z' and part == 2:
                    end = True
                    steps.append(step)
                    break
    return steps

#Part 1

print(*calculate_steps(['AAA'], 1))

#Part 2

positions = [node for node in nodes.keys() if node[2] == 'A']

print(lcm(*calculate_steps(positions, 2)))