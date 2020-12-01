def get_two_sum(nums, target):
    '''
    Search an array for 2 numbers that sum to a target.
    '''
    sorted_nums = sorted(nums)
    idx_left = 0
    idx_right = len(sorted_nums) - 1
    total = sorted_nums[idx_left] + sorted_nums[idx_right]
    
    while total != target:
        if idx_left > idx_right:            
            return None
        elif total < target:
            idx_left += 1
        elif total > target:
            idx_right -= 1
        
        left_num = sorted_nums[idx_left]
        right_num = sorted_nums[idx_right]
        total = left_num + right_num
        
    return left_num, right_num

def get_three_sum(nums, target):
    '''
    Search an array for 3 numbers that sum to a target.
    '''
    sorted_nums = sorted(nums)
    for i, num in enumerate(sorted_nums):
        current_target = target - num
        result = get_two_sum(sorted_nums[i:], current_target)
        if result is not None:
            return (num, *result)
    return None

with open('input.txt') as f:
    nums = [int(line.strip()) for line in f]
    print(get_two_sum(nums, 2020)) # (317, 1703)
    print(get_three_sum(nums, 2020)) # (315, 624, 1081)  
    