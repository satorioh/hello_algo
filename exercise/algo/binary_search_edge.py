"""
二分查找：1.查找左边界
给定一个长度为 n 的有序数组 nums ，其中可能包含重复元素。
请返回数组中最左一个元素 target 的索引。若数组中不包含该元素，则返回 -1 。
"""
nums = [1, 3, 6, 6, 6, 8, 15, 23, 23, 23, 26, 31, 35]
target = 6


def binary_search_insert_duplication(nums: list[int], target: int) -> int:
    """二分查找插入点（存在重复元素）"""
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    # 返回插入点 i
    return i


def binary_search_left_edge(nums: list[int], target: int) -> int:
    """二分查找左边界（有重复元素）"""
    i = binary_search_insert_duplication(nums, target)
    if i == len(nums) or nums[i] != target:
        return -1
    return i


# print(binary_search_left_edge(nums, target))

"""
二分查找：2.查找右边界
"""


def binary_search_right_edge(nums: list[int], target: int) -> int:
    """二分查找最右一个 target"""
    # 转化为查找最左一个 target + 1
    i = binary_search_insert_duplication(nums, target + 1)
    # j 指向最右一个 target ，i 指向首个大于 target 的元素
    j = i - 1
    # 未找到 target ，返回 -1
    if j == -1 or nums[j] != target:
        return -1
    # 找到 target ，返回索引 j
    return j


def binary_search_edge(nums: list[int], target):
    """二分查找边界（存在重复元素）"""
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    # 返回插入点 i
    return j, i


print(binary_search_edge(nums, target - 0.5))
