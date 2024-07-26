"""
二分查找通用算法
"""
nums = [1, 3, 6, 8, 8, 8, 15, 15, 23, 26, 31, 35]
target = 16


def binary_search_common(nums: list[int], target):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    return j, i


def find_num_left_or_index(nums, target):
    j, i = binary_search_common(nums, target)
    print(j, i)
    if nums[i] != target:
        return -1
    return nums[i]


def find_num_right(nums, target):
    j, i = binary_search_common(nums, target)
    print(j, i)
    if nums[j] != target - 0.5:
        return -1
    return nums[j]


print(find_num_left_or_index(nums, target))
print(find_num_right(nums, target + 0.5))
