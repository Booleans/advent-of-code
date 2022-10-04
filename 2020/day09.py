with open("inputs/day09.txt") as f:
    nums = [int(line.strip()) for line in f]

search_nums = nums[:25]
target_nums = nums[25:]

for target in target_nums:
    search_set = set(search_nums)
    two_sum_found = any((target - num) in search_set for num in search_set)

    if two_sum_found:
        search_nums.pop(0)
        search_nums.append(target)
    else:
        print(target)  # Part 1 solution.
        break

idx_left = 0
idx_right = 1
target = 32321523

total = sum(nums[idx_left : idx_right + 1])

while total != target:
    if total < target:
        idx_right += 1
    else:
        idx_left += 1

    total = sum(nums[idx_left : idx_right + 1])

contiguous_nums = nums[idx_left : idx_right + 1]
result = min(contiguous_nums) + max(contiguous_nums)

print(result)  # Part 2 solution.
