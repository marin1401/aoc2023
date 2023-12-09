#Day 04

with open('./04.txt') as my_input:
    input_lines = my_input.readlines()

cards = [card.split(': ')[1].split(' | ') for card in input_lines]

points = []
won_copies = {}
for card, all_numbers in enumerate(cards, 1):
    winning_numbers, my_numbers = (tuple(map(int, numbers.split()))
                                   for numbers in all_numbers)
    intersections = len(set(winning_numbers) & set(my_numbers))
    point = pow(2, intersections-1) if intersections else 0
    points.append(point)
    won_copies[card] = [card+copy+1 for copy in range(intersections)]

#Part 1

print(sum(points))

#Part 2

instances = {}
for card in won_copies.keys():
    scratchcards = 1
    for cards, copies in won_copies.items():
        if card in copies:
            scratchcards += instances[cards]
    instances[card] = scratchcards

print(sum(instances.values()))