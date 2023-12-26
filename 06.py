#Day 06

with open('./06.txt') as my_input:
    input_lines = my_input.readlines()

times = list(map(int, input_lines[0].split()[1:]))
distances = list(map(int, input_lines[1].split()[1:]))

def first_win(time, distance):
    for speed in range(1, time):
        if (time-speed)*speed > distance:
            return speed

def last_win(time, distance):
    for speed in range(time, 1, -1):
        if (time-speed)*speed > distance:
            return speed

#Part 1

wins_multiplied = 1
for time, distance in zip(times, distances):
    wins_multiplied *= last_win(time, distance) - first_win(time, distance) + 1

print(wins_multiplied)

#Part 2

time = int(input_lines[0].replace(' ', '').split(':')[1])
distance = int(input_lines[1].replace(' ', '').split(':')[1])

print(last_win(time, distance) - first_win(time, distance) + 1)