def two_sum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in num_to_index:
            return [num_to_index[difference], index]
        num_to_index[num] = index
    return []
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))