def single_number(nums):
    single = 0
    for num in nums:
        single ^= num
    return single
nums = [4, 1, 2, 1, 2]
print(single_number(nums))