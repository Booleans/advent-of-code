from collections import Counter
from itertools import combinations

with open('inputs/day02.txt') as f:
    boxes = f.read().split('\n')

letter_twice = {box_id for box_id in boxes if 2 in Counter(box_id).values()}
letter_thrice = {box_id for box_id in boxes if 3 in Counter(box_id).values()}

# Part 1 solution.
print(f'{len(letter_twice)} words have a letter that appears exactly twice and {len(letter_thrice)} words have a letter appears exactly thrice.')
print(f'Multiplying the two numbers together yields {len(letter_twice)*(len(letter_thrice))}.')

box_pairs = list(combinations(boxes, 2))
matching_letters = None

for box1, box2 in box_pairs:
    num_differences = sum(box_1_letter != box_2_letter for box_1_letter, box_2_letter in zip(box1, box2))
    if num_differences == 1:
        matching_letters = [box_1_letter for box_1_letter, box_2_letter in zip(box1, box2) if box_1_letter == box_2_letter]
        break

# Part 2 solution.
print(f'The common letters between the two correct box IDs are {"".join(matching_letters)}.')
