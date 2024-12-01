import re
from collections import Counter

with open("inputs/day01.txt") as f:
    raw = f.read()

rows = re.findall(r'(\d+)\s{3}(\d+)', raw)

left_list =  sorted([int(row[0]) for row in rows])
right_list = sorted([int(row[1]) for row in rows])

total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(f'The total distance between the lists is {total_distance}.')

counts = Counter(right_list)

similarity_score = sum(counts[num] * num for num in left_list)

print(f'The similarity score between the two lists is {similarity_score}.')