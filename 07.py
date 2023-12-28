#Day 07

from collections import Counter

with open('./07.txt') as my_input:
    input_lines = my_input.readlines()

hands = [line.split() for line in input_lines]

types = {'high_card': [], 'one_pair': [], 'two_pair': [],
         'three_of_a_kind': [], 'full_house': [], 'four_of_a_kind': [],
         'five_of_a_kind': []}

def calculate_total_winnings(part):
    for cards, bid in hands:
        cards = cards.replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('T', 'A')
        if part == 1:
            cards = cards.replace('J', 'B')
        elif part == 2:
            cards = cards.replace('J', '1')
        hand = cards, bid
        unique_cards = len(set(cards))
        if unique_cards == 5:
            if '1' not in cards:
                types['high_card'].append(hand)
            else:
                types['one_pair'].append(hand)
        elif unique_cards == 4:
            if '1' not in cards:
                types['one_pair'].append(hand)
            else:
                types['three_of_a_kind'].append(hand)
        elif unique_cards == 3:
            if '1' not in cards:
                if 3 not in Counter(cards).values():
                    types['two_pair'].append(hand)
                else:
                    types['three_of_a_kind'].append(hand)
            else:
                if 3 not in Counter(cards).values() and cards.count('1') == 1:
                    types['full_house'].append(hand)
                else:
                    types['four_of_a_kind'].append(hand)
        elif unique_cards == 2:
            if '1' not in cards:
                if 4 not in Counter(cards).values():
                    types['full_house'].append(hand)
                else:
                    types['four_of_a_kind'].append(hand)
            else:
                types['five_of_a_kind'].append(hand)
        else:
            types['five_of_a_kind'].append(hand)

    for key in types.keys():
        types[key].sort()

    winnings = 0
    rank = 1
    for key, value in types.items():
        for cards, bid in types[key]:
            winnings += int(bid)*rank
            rank += 1
        types[key] = []

    return winnings

#Part 1

print(calculate_total_winnings(1))

#Part 2

print(calculate_total_winnings(2))