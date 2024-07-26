"""
哈希优化
给定一个整数数组 nums 和一个目标元素 target ，
请在数组中搜索“和”为 target 的两个元素，并返回它们的数组索引。
返回任意一个解即可。
"""
nums = [2, 7, 11, 15]
target = 22


def two_sum_hash_table(nums, target):
    hash = {}
    nums_len = len(nums)
    for i in range(nums_len):
        key = nums[i]
        sub = target - key
        if sub in hash:
            return [hash[sub], i]
        hash[key] = i


print(two_sum_hash_table(nums, target))
