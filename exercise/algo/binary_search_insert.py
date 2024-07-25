"""
二分查找插入点
给定一个长度为n的有序数组 nums 和一个元素 target ，数组不存在重复元素。
现将 target 插入数组 nums 中，并保持其有序性。
若数组中已存在元素 target ，则插入到其左方。请返回插入后 target 在数组中的索引。
"""
nums = [1, 3, 6, 8, 15, 23, 26, 31, 35]
target = 12


def binary_search_insert(nums: list[int], target: int) -> int:
    """二分查找插入点（无重复元素）"""
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid  # 已存在target，index 就是 mid
    return i  # 不存在target，index 是 i


def binary_search_insertion2(nums: list[int], target: int) -> int:
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


print(binary_search_insert(nums, target))
