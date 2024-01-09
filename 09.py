#Day 09

with open('./09.txt') as my_input:
    input_lines = my_input.readlines()

histories = [list(map(int, line.split())) for line in input_lines]

def get_sum(part):
    levels = []
    value_sum = 0
    for history in histories:
        if part == 1:
            levels.append(history)
        elif part == 2:
            levels.append(history[::-1])
        while set(levels[-1]) != {0}:
            levels.append([b-a for a, b in zip(levels[-1], levels[-1][1:])])
        value_sum += sum(level[-1] for level in reversed(levels[:-1]))
        levels = []
    return value_sum

#Part 1

print(get_sum(1))

#Part 2

print(get_sum(2))