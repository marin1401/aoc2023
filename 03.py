#Day 03

with open('./03.txt') as my_input:
    input_lines = my_input.read().splitlines()

symbol_positions = []
numbers = []
number = ''
for y, line in enumerate(input_lines):
    for x, char in enumerate(line):
        if char.isdigit():
            number += char
            if x == len(line) - 1:
                numbers.append(((y, x-1), int(number)))
                number = ''
            continue
        elif char != '.':
            symbol_positions.append(((y, x), char))
        if number:
            numbers.append(((y, x-1), int(number)))
            number = ''

part_numbers = []
gear_ratios = []
for (ys, xs), symbol in symbol_positions:
    gear_ratio = 0
    for (yn, xn), number in numbers:
        if yn in range(ys-1, ys+2):
            if xs in range(xn-len(str(number)), xn+2):
                part_numbers.append(number)
                if symbol == '*':
                    if not gear_ratio:
                        gear_ratio = number
                    else:
                        gear_ratio *= number
                        gear_ratios.append(gear_ratio)

#Part 1

print(sum(part_numbers))

#Part 2

print(sum(gear_ratios))