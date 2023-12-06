#Day 01

with open('./01.txt') as my_input:
    input_lines = my_input.readlines()

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
stigid = ['eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']

def get_digit(line, part, list_of_digits):
    string = ''
    for char in line:
        if char.isdigit():
            return char
        elif part == 2:
            string += char
            number = get_number(string, list_of_digits)
            if number:
                return number

def get_number(string, list_of_digits):
    for i in range(3, 6):
        if len(string) > i-1:
            if string[-i:] in list_of_digits:
                return str(list_of_digits.index(string[-i:]) + 1)

def get_calibration_values_sum(part):
    calibration_values_sum = 0
    for line in input_lines:
        first_digit = get_digit(line, part, digits)
        last_digit = get_digit(line[::-1], part, stigid)
        calibration_values_sum += int(first_digit + last_digit)
    return calibration_values_sum


#Part 1

print(get_calibration_values_sum(1))

#Part 2

print(get_calibration_values_sum(2))