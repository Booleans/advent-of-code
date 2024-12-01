from collections import Counter

with open("inputs/day01.txt") as f:
    raw = f.read().split()

nums = [int(num) for  num in raw]

left_list = sorted(nums[0::2])
right_list = sorted(nums[1::2])

total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))

print(f'The total distance between the lists is {total_distance}.')

counts = Counter(right_list)

similarity_score = sum(counts[num] * num for num in left_list)

print(f'The similarity score between the two lists is {similarity_score}.')